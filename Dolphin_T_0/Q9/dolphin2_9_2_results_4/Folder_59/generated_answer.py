def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst[0:10]) if num % 2 != 0]