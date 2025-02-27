def if_contains_anagrams(str_list):
    anagrams = []
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i].lower()
            str2 = str_list[j].lower()
            if sorted(str1) == sorted(str2) and len(str1) >= 3 and (len(str2) >= 3):
                anagrams.append((i, j))
    if len(anagrams) >= 106:
        return True
    else:
        return False