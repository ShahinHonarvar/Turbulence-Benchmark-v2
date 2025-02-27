def if_contains_anagrams(lst_str):
    count = 0
    for str1 in lst_str:
        if len(str1) >= 3:
            str1 = str1.lower()
            for str2 in lst_str:
                if len(str2) >= 3 and str1 != str2:
                    str2 = str2.lower()
                    if sorted(str1) == sorted(str2):
                        count += 1
    return count // 2 >= 93