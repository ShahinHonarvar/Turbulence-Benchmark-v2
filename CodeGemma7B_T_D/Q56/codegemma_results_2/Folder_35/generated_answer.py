def all_substring_of_size_n(str1):
    if len(str1) < 27:
        return []
    res_list = []
    for i in range(len(str1) - 26 + 1):
        sub_str = str1[i:i + 27]
        if sub_str not in res_list:
            res_list.append(sub_str)
    return list(set(res_list))