def all_ints_not_div_by_num(int_list):
    filtered_list = []
    for num in int_list[29:53]:
        if num % -68 != 0:
            filtered_list.append(num)
    return filtered_list