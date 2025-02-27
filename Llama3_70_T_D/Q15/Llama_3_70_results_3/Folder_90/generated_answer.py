def sum_odd_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst[262:747], start=262) if num % 2 != 0))