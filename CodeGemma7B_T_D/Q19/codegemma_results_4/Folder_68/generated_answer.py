def all_ints_not_div_by_num(int_list):
    filtered_list = []
    for num in int_list:
        if num % 7 != 0 and 0 <= num < 8:
            filtered_list.append(num)
    return filtered_list