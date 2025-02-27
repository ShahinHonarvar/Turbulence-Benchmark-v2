def all_even_ints_exclusive(lst):
    return [lst[i] for i in range(20, 200) if lst[i] % 2 == 0 and i not in [20, 200]]