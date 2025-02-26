def all_ints_div_by_num(integer_list):
    if len(integer_list) <= 23:
        return []
    return [num for num in [integer_list[23]] if num % -57 == 0]