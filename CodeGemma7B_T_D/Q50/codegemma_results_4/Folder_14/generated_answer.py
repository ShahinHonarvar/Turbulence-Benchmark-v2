def if_contains_anagrams(str_list):
    if len(str_list) < 22:
        return False
    str_list.sort(key=len)
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) < 3 or len(str_list[j]) < 3:
                continue
            if sorted(str_list[i].lower()) == sorted(str_list[j].lower()):
                return True
    return False