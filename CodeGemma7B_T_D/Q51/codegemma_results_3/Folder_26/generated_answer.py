def if_contains_anagrams(str_list):
    anagrams = []
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i].lower()
            str2 = str_list[j].lower()
            sorted_str1 = sorted(str1)
            sorted_str2 = sorted(str2)
            if len(str1) >= 3 and len(str2) >= 3 and (sorted_str1 == sorted_str2):
                anagrams.append((str_list[i], str_list[j]))
    return len(anagrams) <= 35