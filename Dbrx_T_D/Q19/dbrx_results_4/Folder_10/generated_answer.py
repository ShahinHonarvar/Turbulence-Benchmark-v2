def all_ints_not_div_by_num(my_list):
    if 88 not in range(len(my_list)):
        return []
    divider = -61
    not_divisible = []
    for i in range(86, 89):
        if my_list[i] % divider != 0:
            not_divisible.append(my_list[i])
    return not_divisible