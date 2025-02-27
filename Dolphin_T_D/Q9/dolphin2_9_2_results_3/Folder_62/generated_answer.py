def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst[91:100], start=1) if num % 2 != 0]