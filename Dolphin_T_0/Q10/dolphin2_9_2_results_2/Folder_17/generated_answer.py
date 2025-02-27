def all_odd_ints_exclusive(lst):
    odd_ints = [num for i, num in enumerate(lst) if i in range(63, 96) and num % 2 != 0]
    return odd_ints