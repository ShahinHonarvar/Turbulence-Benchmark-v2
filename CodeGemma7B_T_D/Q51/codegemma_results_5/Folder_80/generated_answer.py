def if_contains_anagrams(str_list):
    anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i].lower()) == len(str_list[j].lower()) and sorted(str_list[i].lower()) == sorted(str_list[j].lower()):
                anagram_pairs += 1
    return anagram_pairs <= 255