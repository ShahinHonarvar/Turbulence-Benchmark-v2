def sum_odd_ints_inclusive(lst):
    if len(lst) <= max(56, 98):
        return 0
    return sum((num for num in lst[56:99:2]))