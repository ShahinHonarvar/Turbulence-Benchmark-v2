def if_contains_anagrams(str_list):
    anagram_pairs = 0
    for str1 in str_list:
        for str2 in str_list:
            if str1 != str2 and sorted(str1.lower()) == sorted(str2.lower()) and (len(str1) >= 3) and (len(str2) >= 3):
                anagram_pairs += 1
    return anagram_pairs >= 61