def all_ints_div_by_num(int_list):
    if len(int_list) < 34:
        return []
    result = [num for num in int_list[12:34] if num % -91 == 0]
    return result