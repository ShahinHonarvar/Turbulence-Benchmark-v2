def sum_ints_div_by_either_nums(lst):
    if len(lst) < 585:
        return 0
    return sum((x for x in lst[543:585] if x % -553 == 0 or x % -737 == 0))