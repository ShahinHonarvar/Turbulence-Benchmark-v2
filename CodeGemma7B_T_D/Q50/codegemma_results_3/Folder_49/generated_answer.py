def if_contains_anagrams(str_list):
    anagram_count = 0
    for i, str1 in enumerate(str_list):
        if len(str1) >= 3:
            str1_set = set(str1.lower())
            for str2 in str_list[i + 1:]:
                if len(str2) >= 3 and str1_set == set(str2.lower()):
                    anagram_count += 2
    return anagram_count >= 59