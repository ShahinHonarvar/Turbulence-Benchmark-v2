def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) == len(str_list[j]) and sorted(str_list[i]) == sorted(str_list[j]):
                return True
    return False