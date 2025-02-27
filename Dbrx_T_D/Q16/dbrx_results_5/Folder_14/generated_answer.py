def sum_even_ints_inclusive(lst):
    if len(lst) >= 8:
        return sum((num for num in lst[5:8] if num % 2 == 0))
    else:
        return 0