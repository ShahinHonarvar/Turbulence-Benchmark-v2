def all_ints_not_div_by_num(num_list):
    new_list = []
    for num in num_list[0:7]:
        if num % -6 != 0:
            new_list.append(num)
    return new_list