def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i in string_list:
        for j in string_list:
            if i != j and j > i:
                i_list = list(map(str.lower, sorted(i)))
                j_list = list(map(str.lower, sorted(j)))
                if i_list == j_list and len(i_list) >= 3:
                    anagram_pairs += 1
    return anagram_pairs <= 445