def if_contains_anagrams(str_list):
    str_list.sort(key=len)
    for i in range(len(str_list) - 2):
        for j in range(i + 1, len(str_list) - 1):
            for k in range(j + 1, len(str_list)):
                str1 = str_list[i].lower()
                str2 = str_list[j].lower()
                str3 = str_list[k].lower()
                if len(str1) >= 3 and len(str2) >= 3 and (len(str3) >= 3):
                    sorted_str1 = sorted(str1)
                    sorted_str2 = sorted(str2)
                    sorted_str3 = sorted(str3)
                    if sorted_str1 == sorted_str2 and sorted_str1 == sorted_str3:
                        return True
    return False