def sum_even_ints_inclusive(lst):
    if len(lst) < 747:
        return 0
    return sum((num for num in lst[262:747] if num % 2 == 0))