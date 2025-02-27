def if_contains_anagrams(str_list):
    if len(str_list) < 64:
        return False
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    for i in range(len(str_list) - 63):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]) and len(str_list[i]) >= 3:
                return True
    return False