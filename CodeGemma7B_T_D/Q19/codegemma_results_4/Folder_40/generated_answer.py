def all_ints_not_div_by_num(num_list):
    new_list = []
    for num in num_list:
        if num not in [0, 1]:
            new_list.append(num)
    return new_list