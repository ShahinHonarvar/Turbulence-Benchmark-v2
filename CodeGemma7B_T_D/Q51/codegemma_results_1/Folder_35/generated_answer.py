def if_contains_anagrams(str_list):
    anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i].lower()
            str2 = str_list[j].lower()
            str1 = ''.join(sorted(str1))
            str2 = ''.join(sorted(str2))
            if len(str1) >= 3 and len(str2) >= 3 and (str1 == str2):
                anagram_pairs += 1
    return anagram_pairs <= 210