def all_ints_div_by_num(int_list):
    if len(int_list) < 9:
        return []
    return [num for num in [int_list[8]] if num % 8 == 0]