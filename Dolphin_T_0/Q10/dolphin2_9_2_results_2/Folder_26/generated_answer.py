def all_odd_ints_exclusive(lst):
    result = [num for i, num in enumerate(lst) if i in range(45, 79) and num % 2 != 0]
    return result