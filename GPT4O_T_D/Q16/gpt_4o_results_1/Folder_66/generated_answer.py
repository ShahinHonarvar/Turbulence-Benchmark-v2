def sum_even_ints_inclusive(lst):
    return sum((num for num in lst[50:55] if num % 2 == 0)) if len(lst) >= 55 else 0