def all_odd_ints_inclusive(lst):
    return [lst[i] for i in range(42, 69) if i < len(lst) and lst[i] % 2 != 0]