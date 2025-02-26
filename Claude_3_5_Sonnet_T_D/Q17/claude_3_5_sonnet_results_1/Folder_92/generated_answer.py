def all_ints_div_by_both_two_nums(integer_list):
    if not integer_list:
        return []
    return [integer_list[0]] if integer_list[0] % 1 == 0 and integer_list[0] % -1 == 0 else []