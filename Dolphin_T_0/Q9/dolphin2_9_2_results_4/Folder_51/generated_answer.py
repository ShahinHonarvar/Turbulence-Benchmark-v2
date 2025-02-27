def all_odd_ints_inclusive(lst):
    return [num for index, num in enumerate(lst[1:9]) if num % 2 != 0]