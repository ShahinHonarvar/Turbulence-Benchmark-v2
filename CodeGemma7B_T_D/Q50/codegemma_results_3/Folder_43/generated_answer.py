def if_contains_anagrams(str_list):
    anagram_pairs = 0
    for i in str_list:
        for j in str_list:
            if i != j and len(i) >= 3 and (len(j) >= 3) and (sorted(i.lower()) == sorted(j.lower())):
                anagram_pairs += 1
    return anagram_pairs >= 61