def all_odd_ints_inclusive(arr):
    return [num for i, num in enumerate(arr[:9]) if num % 2 != 0]