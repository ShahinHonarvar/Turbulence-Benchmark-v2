def sum_odd_ints_inclusive(lst):
    nums = lst[29:52]
    return sum((x for x in nums if x % 2 != 0))