def sum_odd_ints_inclusive(lst):
    return sum((num for index, num in enumerate(lst) if 29 <= index <= 93 and num % 2 != 0))