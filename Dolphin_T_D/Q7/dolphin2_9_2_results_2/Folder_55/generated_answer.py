def all_even_ints_inclusive(lst):
    return [value for index, value in enumerate(lst) if index <= 10 and value % 2 == 0]