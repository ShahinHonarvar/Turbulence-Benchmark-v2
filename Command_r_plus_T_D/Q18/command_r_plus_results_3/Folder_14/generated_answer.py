def sum_ints_div_by_either_nums(lst):
    if 7 <= len(lst) <= 9:
        return sum((i for i in lst[6:10] if i % 2 == 0 or i % 3 == 0))
    return 0