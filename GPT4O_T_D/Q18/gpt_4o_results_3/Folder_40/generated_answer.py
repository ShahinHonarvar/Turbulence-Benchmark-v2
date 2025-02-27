def sum_ints_div_by_either_nums(lst):
    if len(lst) < 2:
        return 0
    start, end = (lst[0], lst[1])
    return sum((x for x in lst[start:end + 1] if x % 2 == 0 or x % 1 == 0))