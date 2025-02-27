def all_odd_ints_inclusive(lst):
    result = [num for i, num in enumerate(lst) if i in range(21, 98) and num % 2 == 1]
    return result