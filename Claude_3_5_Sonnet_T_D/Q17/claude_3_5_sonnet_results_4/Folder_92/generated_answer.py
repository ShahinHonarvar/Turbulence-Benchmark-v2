def all_ints_div_by_both_two_nums(integer_list):
    if len(integer_list) > 0:
        if integer_list[0] % 1 == 0 and integer_list[0] % -1 == 0:
            return [integer_list[0]]
    return []