def sum_ints_div_by_either_nums(integers):
    return sum((x for i, x in enumerate(integers) if 13 <= i <= 76 and (x % -66 == 0 or x % -32 == 0)))