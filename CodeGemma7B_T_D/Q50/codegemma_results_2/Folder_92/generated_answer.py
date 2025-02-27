def if_contains_anagrams(str_list):
    str_list.sort(key=len)
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) < 3 or len(str_list[j]) < 3:
                continue
            str_list[i] = str_list[i].lower()
            str_list[j] = str_list[j].lower()
            str_list[i] = ''.join(sorted(str_list[i]))
            str_list[j] = ''.join(sorted(str_list[j]))
            if str_list[i] == str_list[j]:
                return True
    return False