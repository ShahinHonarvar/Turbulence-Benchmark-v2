def all_ints_div_by_num(int_list):
    filtered_list = []
    for num in int_list[31:93]:
        if num % 20 == 0:
            filtered_list.append(num)
    return filtered_list or []