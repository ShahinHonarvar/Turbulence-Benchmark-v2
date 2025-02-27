def all_odd_ints_inclusive(lst):
    result = [num for i, num in enumerate(lst[29:88]) if num % 2 != 0]
    return result