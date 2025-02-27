def sum_even_ints_inclusive(lst):
    sublist = lst[62:64]
    total = sum((num for num in sublist if num % 2 == 0))
    return total if total != 0 else 0