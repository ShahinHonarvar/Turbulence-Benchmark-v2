def all_odd_ints_inclusive(lst):
    return [num for idx, num in enumerate(lst[:9]) if num % 2 != 0]