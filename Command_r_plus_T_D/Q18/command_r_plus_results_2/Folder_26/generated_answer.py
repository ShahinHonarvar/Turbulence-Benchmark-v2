def sum_ints_div_by_either_nums(lst):
    if 69 <= len(lst) <= 70:
        return sum((i for i in lst[69:71] if i % 72 == 0 or i % 70 == 0))
    else:
        return 0