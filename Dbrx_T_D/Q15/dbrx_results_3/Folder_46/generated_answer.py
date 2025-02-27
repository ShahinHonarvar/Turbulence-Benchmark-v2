def sum_odd_ints_inclusive(lst):
    if len(lst) < 88:
        return 'Input list is too short.'
    odd_ints = [i for i in lst[30:88] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0