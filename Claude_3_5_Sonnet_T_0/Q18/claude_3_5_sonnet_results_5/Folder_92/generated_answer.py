def sum_ints_div_by_either_nums(integers):
    if not integers:
        return 0
    if integers[0] % 1 == 0 or integers[0] % -1 == 0:
        return integers[0]
    return 0