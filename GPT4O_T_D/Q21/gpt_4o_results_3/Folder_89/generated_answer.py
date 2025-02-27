def all_ints_div_by_num(int_list):
    if len(int_list) < 60:
        return []
    return [num for num in int_list[30:60] if num % 39 == 0]