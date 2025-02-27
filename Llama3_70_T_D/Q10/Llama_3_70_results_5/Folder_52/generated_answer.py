def all_odd_ints_exclusive(lst):
    return [lst[i] for i in range(94, len(lst)) if i not in range(93) and lst[i] % 2 != 0]