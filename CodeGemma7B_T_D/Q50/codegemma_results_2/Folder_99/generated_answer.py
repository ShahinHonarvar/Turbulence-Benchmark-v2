def if_contains_anagrams(str_list):
    str_list.sort(key=lambda s: len(s))
    anagram_pairs = 0
    for i in range(len(str_list) - 2):
        for j in range(i + 1, len(str_list) - 1):
            for k in range(j + 1, len(str_list)):
                str1, str2, str3 = (str_list[i].lower(), str_list[j].lower(), str_list[k].lower())
                if sorted(str1) == sorted(str2) == sorted(str3) and len(str1) >= 3:
                    anagram_pairs += 1
    return anagram_pairs >= 314