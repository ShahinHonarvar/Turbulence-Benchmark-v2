def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst[26:53], 26) if num % 2 != 0))