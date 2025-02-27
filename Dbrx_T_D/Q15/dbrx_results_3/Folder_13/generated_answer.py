def sum_odd_ints_inclusive(lst):
    if not isinstance(lst, list) or len(lst) < 88:
        return 0
    odd_ints = [i for i in lst[24:88] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0