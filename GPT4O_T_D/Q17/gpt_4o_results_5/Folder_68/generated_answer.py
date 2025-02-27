def all_ints_div_by_both_two_nums(lst):
    if len(lst) < 8:
        return []
    result = [x for x in lst[7:8] if x % 5 == 0 and x % 7 == 0]
    return result