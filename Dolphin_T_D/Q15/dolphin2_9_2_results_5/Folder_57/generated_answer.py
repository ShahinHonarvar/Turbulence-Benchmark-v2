def sum_odd_ints_inclusive(lst):
    valid_range = lst[27:56]
    odd_ints = [n for n in valid_range if n % 2 != 0]
    return sum(odd_ints) if odd_ints else 0