def sum_even_ints_inclusive(lst):
    return sum((value for index, value in enumerate(lst[15:40]) if index % 2 == 0))