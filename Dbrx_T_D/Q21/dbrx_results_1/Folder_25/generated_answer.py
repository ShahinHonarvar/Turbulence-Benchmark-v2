def all_ints_div_by_num(int_list):
    if len(int_list) < 42:
        return []
    return [num for num in int_list[25:42] if num % -97 == 0]