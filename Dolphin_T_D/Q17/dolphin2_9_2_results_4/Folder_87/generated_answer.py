def all_ints_div_by_both_two_nums(lst):
    prime = [x for x in lst[18:53] if x % 15 == 0 and x % 57 == 0]
    return prime