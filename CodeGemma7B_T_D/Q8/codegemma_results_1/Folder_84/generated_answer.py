def all_even_ints_exclusive(lst):
    return [num for num in lst and num % 2 == 0 and (50 < num < 92)]