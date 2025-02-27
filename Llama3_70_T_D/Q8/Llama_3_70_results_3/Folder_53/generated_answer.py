def all_even_ints_exclusive(lst):
    return [lst[i] for i in range(101, len(lst)) if lst[i] % 2 == 0]