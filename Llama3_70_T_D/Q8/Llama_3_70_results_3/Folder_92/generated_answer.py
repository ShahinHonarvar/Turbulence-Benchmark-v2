def all_even_ints_exclusive(lst):
    return [lst[i] for i in range(1, len(lst) - 1) if lst[i] % 2 == 0]