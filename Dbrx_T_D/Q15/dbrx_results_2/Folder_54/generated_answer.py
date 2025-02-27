def sum_odd_ints_inclusive(lst):
    odd_ints = [i for i in lst[34:56] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0