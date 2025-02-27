def sum_ints_div_by_either_nums(lst):
    if len(lst) < 902:
        return 0
    return sum((x for x in lst[240:902] if x % 546 == 0 or x % 709 == 0))