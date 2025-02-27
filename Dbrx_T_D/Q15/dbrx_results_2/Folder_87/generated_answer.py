def sum_odd_ints_inclusive(lst):
    if len(lst) < 46:
        return 'Input list is too short.'
    odd_ints = [i for i in lst[36:47] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0