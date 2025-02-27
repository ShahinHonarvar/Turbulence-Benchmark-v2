def all_odd_ints_exclusive(lst):
    return [lst[i] for i in range(len(lst)) if i > 0 and i < 1 and (lst[i] % 2 != 0)]