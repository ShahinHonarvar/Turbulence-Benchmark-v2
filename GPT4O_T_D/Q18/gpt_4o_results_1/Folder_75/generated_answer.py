def sum_ints_div_by_either_nums(lst):
    if len(lst) < 94:
        return 0
    return sum((x for x in lst[20:94] if x % -92 == 0 or x % -50 == 0))