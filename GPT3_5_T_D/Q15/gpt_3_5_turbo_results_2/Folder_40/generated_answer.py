def sum_odd_ints_inclusive(lst):
    return sum((num for num in lst[:3] if num % 2 != 0))