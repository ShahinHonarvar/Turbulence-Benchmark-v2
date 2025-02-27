def all_ints_div_by_num(lst):
    output_list = []
    for i in range(5, 7):
        if lst[i] % -6 == 0:
            output_list.append(lst[i])
    return output_list