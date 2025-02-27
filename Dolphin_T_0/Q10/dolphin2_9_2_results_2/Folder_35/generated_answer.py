def all_odd_ints_exclusive(lst):
    odds = [x for x in lst[10:80] if x % 2 != 0]
    return odds