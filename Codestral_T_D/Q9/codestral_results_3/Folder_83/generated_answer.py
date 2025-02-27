def all_odd_ints_inclusive(lst):
    return [num for idx, num in enumerate(lst[90:201]) if num % 2 != 0]