def all_odd_ints_inclusive(lst):
    result = [num for index, num in enumerate(lst) if 59 <= index <= 97 and num % 2 != 0]
    return result