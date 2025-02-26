def all_ints_div_by_num(int_list):
    if len(int_list) < 2:
        return []
    return [num for num in int_list[:2] if num % 2 == 0]