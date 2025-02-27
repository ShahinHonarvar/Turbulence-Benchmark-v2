def all_ints_div_by_num(int_list):
    new_list = []
    for num in int_list[29:52]:
        if num % -37 == 0:
            new_list.append(num)
    return new_list