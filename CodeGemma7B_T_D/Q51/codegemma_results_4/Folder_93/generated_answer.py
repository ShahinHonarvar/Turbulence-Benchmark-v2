def if_contains_anagrams(str_list):
    anagram_pairs = set()
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = ''.join(sorted(str_list[i].lower()))
            str2 = ''.join(sorted(str_list[j].lower()))
            if len(str1) >= 3 and len(str2) >= 3 and (str1 == str2):
                anagram_pairs.add((i, j))
    return len(anagram_pairs) <= 36