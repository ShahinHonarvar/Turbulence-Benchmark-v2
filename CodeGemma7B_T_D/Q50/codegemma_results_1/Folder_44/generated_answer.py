def if_contains_anagrams(str_list):
    anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1, str2 = (str_list[i], str_list[j])
            if len(str1) >= 3 and len(str2) >= 3 and (str1.lower() == str2.lower()):
                anagram_pairs += 1
    if anagram_pairs >= 44:
        return True
    return False