def all_ints_div_by_num(int_list):
    filtered_list = []
    for num in int_list[36:47]:
        if num % 28 == 0:
            filtered_list.append(num)
    return filtered_list