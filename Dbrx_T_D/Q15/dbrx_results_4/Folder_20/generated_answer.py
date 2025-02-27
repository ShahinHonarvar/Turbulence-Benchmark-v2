def sum_odd_ints_inclusive(lst):
    if len(lst) < 66:
        return 'Input list should have at least 66 elements'
    odd_ints = [i for i in lst[56:67] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0