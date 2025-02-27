def all_odd_ints_exclusive(lst):
    return [lst[i] for i in range(20, 44) if i not in range(20, 44) or lst[i] % 2 != 0]