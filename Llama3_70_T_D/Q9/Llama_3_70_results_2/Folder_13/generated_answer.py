def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if i >= 25 and i <= 87 and (num % 2 != 0)]