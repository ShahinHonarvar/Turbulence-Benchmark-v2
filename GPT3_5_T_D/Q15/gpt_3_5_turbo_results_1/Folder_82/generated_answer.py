def sum_odd_ints_inclusive(lst):
    return sum((num for num in lst[20:201] if num % 2 != 0))