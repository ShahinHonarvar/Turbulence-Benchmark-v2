def all_odd_ints_exclusive(lst):
    return [lst[i] for i in range(369, 983) if i < len(lst) and lst[i] % 2 != 0]