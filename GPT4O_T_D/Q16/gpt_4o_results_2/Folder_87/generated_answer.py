def sum_even_ints_inclusive(lst):
    if 36 > len(lst) - 1:
        return 0
    sublist = lst[36:min(47, len(lst))]
    return sum((num for num in sublist if num % 2 == 0))