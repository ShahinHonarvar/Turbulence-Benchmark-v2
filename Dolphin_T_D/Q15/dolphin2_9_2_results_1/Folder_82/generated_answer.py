def sum_odd_ints_inclusive(lst):
    result = sum((num for num in lst[20:201] if num % 2 != 0))
    return result if result else 0