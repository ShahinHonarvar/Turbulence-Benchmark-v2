def if_contains_anagrams(str_list):
    if len(str_list) < 19:
        return False
    str_list = sorted(str_list, key=len)
    for i, str1 in enumerate(str_list):
        for j in range(i + 1, len(str_list)):
            str2 = str_list[j]
            if abs(len(str1) - len(str2)) > 2:
                continue
            str1 = sorted(str1.lower())
            str2 = sorted(str2.lower())
            if str1 == str2 and str1 != str2:
                if sorted([str1, str2], key=len)[-1] - sorted([str1, str2], key=len)[0] < 3:
                    return True
    return False