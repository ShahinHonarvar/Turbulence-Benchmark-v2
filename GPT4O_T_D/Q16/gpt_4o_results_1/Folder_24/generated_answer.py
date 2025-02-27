def sum_even_ints_inclusive(lst):
    if len(lst) < 96:
        return 0
    return sum((num for num in lst[74:96] if num % 2 == 0))