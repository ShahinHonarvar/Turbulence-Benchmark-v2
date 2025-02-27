def sum_even_ints_inclusive(lst):
    if len(lst) < 7:
        return 0
    subset = lst[6:7]
    return sum((num for num in subset if num % 2 == 0))