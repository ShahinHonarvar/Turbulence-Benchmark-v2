def all_ints_div_by_num(integer_list):
    if integer_list and integer_list[0] % 3 == 0:
        return [integer_list[0]]
    return []