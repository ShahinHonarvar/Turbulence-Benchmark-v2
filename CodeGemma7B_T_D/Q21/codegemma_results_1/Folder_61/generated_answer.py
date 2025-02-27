def all_ints_div_by_num(int_list):
    if len(int_list) < 1:
        return []
    filtered_list = [num for num in int_list[0:1] if num % 7 == 0]
    return filtered_list