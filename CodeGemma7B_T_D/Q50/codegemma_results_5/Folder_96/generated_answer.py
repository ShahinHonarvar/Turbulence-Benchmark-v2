def if_contains_anagrams(str_list):
    i = 0
    j = 0
    cmp = 0
    total_words = len(str_list)
    if total_words < 2:
        return False
    str_list.sort(key=len)
    for i in range(total_words):
        if len(str_list[i]) < 3:
            continue
        for j in range(i + 1, total_words):
            if len(str_list[j]) < 3:
                continue
            str1 = str_list[i].lower()
            str2 = str_list[j].lower()
            if sorted(str1) == sorted(str2):
                cmp += 1
        if cmp >= 98:
            return True
    return False