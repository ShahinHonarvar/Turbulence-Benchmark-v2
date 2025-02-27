def if_contains_anagrams(str_list):
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                str_list[i] = sorted(str_list[i].lower())
                str_list[j] = sorted(str_list[j].lower())
                if str_list[i] == str_list[j]:
                    return True
    return False