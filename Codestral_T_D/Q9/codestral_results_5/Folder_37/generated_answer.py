def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst[1:6]) if num % 2 != 0]