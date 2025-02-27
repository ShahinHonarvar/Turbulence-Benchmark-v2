def all_odd_ints_exclusive(lst):
    odd_ints = [num for i, num in enumerate(lst) if i > 295 and i < 573 and (num % 2 != 0)]
    return odd_ints