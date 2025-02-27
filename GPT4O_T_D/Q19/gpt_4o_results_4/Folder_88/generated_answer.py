def all_ints_not_div_by_num(int_list):
    if len(int_list) <= 5:
        return []
    return [num for num in int_list[5:7] if num % -6 != 0]