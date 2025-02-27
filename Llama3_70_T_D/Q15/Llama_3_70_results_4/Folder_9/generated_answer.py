def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst[70:201]) if num % 2 != 0))