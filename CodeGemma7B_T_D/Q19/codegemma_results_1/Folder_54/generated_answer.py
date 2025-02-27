def all_ints_not_div_by_num(int_list):
    new_list = []
    for num in int_list[19:94]:
        if num % 32 != 0:
            new_list.append(num)
    return new_list