def if_contains_anagrams(str_list):
    str_list.sort(key=len)
    for i in range(len(str_list) - 5):
        if str_list[i + 3] + str_list[i + 4] + str_list[i + 5] + str_list[i + 6] + str_list[i + 7] + str_list[i + 8] == str_list[i] + str_list[i + 1] + str_list[i + 2]:
            return True
    return False