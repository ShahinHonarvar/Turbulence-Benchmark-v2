def all_ints_not_div_by_num(list):
    filtered_list = []
    for i in range(32, 54):
        if list[i] % -97 != 0:
            filtered_list.append(list[i])
    if len(filtered_list) == 0:
        return []
    else:
        return filtered_list