def sum_odd_ints_inclusive(lst):
    if len(lst) < 79:
        return 'List is not long enough'
    return sum((x for x in lst[29:80] if x % 2 != 0))