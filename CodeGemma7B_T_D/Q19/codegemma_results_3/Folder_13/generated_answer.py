def all_ints_not_div_by_num(int_list):
    if not int_list or len(int_list) < 34:
        return []
    return [num for num in int_list[32:44] if num % 34 != 0]