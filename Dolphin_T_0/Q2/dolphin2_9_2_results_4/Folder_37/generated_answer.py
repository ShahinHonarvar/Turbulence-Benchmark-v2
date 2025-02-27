def all_ints_exclusive(arr):
    return [num for i, num in enumerate(arr) if i != 0 and i != 8 and (num % 2 != 0)]