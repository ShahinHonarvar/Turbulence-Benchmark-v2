def all_ints_div_by_both_two_nums(lst):
    if len(lst) < 10:
        return []
    return [n for n in lst[8:10] if n % 6 == 0]