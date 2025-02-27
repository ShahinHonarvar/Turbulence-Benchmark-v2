def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst[385:999]) if num % 2 != 0]