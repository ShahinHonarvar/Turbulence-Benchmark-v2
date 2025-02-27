def all_ints_div_by_both_two_nums(list):
    new_list = []
    for i in range(34, 70):
        if list[i] % 19 == 0 and list[i] % 32 == 0:
            new_list.append(list[i])
    if len(new_list) == 0:
        return []
    return new_list