def if_contains_anagrams(str_list):
    str_list = sorted(str_list, key=len)
    anagram_pairs = set()
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i].lower()
            str2 = str_list[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
                anagram_pairs.add((str1, str2))
    if len(anagram_pairs) >= 30:
        return True
    else:
        return False