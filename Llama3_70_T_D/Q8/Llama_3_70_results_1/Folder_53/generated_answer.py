def all_even_ints_exclusive(lst):
    return [lst[i] for i in range(100, len(lst)) if lst[i] % 2 == 0]