def all_odd_ints_exclusive(lst):
    return [lst[i] for i in range(94, len(lst)) if lst[i] % 2 != 0]