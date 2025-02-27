def if_contains_anagrams(str_list):
    anagrams = []
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                str1 = sorted(str_list[i].lower())
                str2 = sorted(str_list[j].lower())
                if str1 == str2:
                    anagrams.append((str_list[i], str_list[j]))
    return len(anagrams) >= 96