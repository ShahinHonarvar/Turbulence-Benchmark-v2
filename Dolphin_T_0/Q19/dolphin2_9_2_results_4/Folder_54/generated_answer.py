def all_ints_not_div_by_num(useful_numbers):
    return [x for i, x in enumerate(useful_numbers) if 19 < i < 94 and x % -32 != 0]