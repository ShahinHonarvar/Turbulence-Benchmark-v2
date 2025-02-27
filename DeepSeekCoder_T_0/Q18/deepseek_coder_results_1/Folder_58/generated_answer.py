def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[240:902] if x % 546 == 0 or x % 709 == 0))