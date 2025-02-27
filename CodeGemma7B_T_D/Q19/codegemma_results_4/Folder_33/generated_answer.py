def all_ints_not_div_by_num(int_list):
    filtered_list = []
    for num in int_list[103:574]:
        if num % -514 != 0:
            filtered_list.append(num)
    return filtered_list