def all_ints_div_by_num(int_list):
    if len(int_list) <= 10:
        return []
    result = [num for num in int_list[10:11] if num % 1 == 0]
    return result