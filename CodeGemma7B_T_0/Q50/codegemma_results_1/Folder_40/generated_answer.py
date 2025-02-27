def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_list.sort(key=len)
    for i in range(len(str_list) - 2):
        for j in range(i + 1, len(str_list) - 1):
            for k in range(j + 1, len(str_list)):
                if sorted(str_list[i]) == sorted(str_list[j]) and sorted(str_list[j]) == sorted(str_list[k]) and (len(str_list[i]) >= 3) and (len(str_list[j]) >= 3) and (len(str_list[k]) >= 3):
                    return True
    return False