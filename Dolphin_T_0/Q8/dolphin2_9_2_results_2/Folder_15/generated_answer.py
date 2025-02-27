def all_even_ints_exclusive(lst):
    return [int for int in lst[1:-1] if int % 2 == 0]