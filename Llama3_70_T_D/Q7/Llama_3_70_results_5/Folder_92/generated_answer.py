def all_even_ints_inclusive(lst):
    return [lst[i] for i in range(min(2, len(lst))) if lst[i] % 2 == 0]