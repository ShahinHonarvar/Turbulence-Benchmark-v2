def sum_odd_ints_inclusive(lst):
    if len(lst) < 36:
        return 'Input list must have at least 36 elements'
    odd_ints = [i for i in lst[32:36] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0