def if_contains_anagrams(str_list):
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            s1 = str_list[i].lower()
            s2 = str_list[j].lower()
            if len(s1) >= 3 and len(s2) >= 3 and (s1 != s2) and (sorted(s1) == sorted(s2)):
                str_list.remove(str_list[j])
    return len(str_list) <= 36