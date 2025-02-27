def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst[30:201]) if i % 2 != 0 and num % 2 != 0]