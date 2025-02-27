def all_odd_ints_inclusive(lst):
    return [num for index, num in enumerate(lst) if 80 <= index <= 200 and num % 2 != 0]