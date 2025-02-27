def all_even_ints_inclusive(list_of_ints):
    return [i for i in list_of_ints if i % 2 == 0 and i >= 0 and (i <= 9)]