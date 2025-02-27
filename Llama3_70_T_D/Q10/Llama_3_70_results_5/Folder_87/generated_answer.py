def all_odd_ints_exclusive(lst):
    return [lst[i] for i in range(32, 99) if i not in range(32, 99) or lst[i] % 2 != 0]