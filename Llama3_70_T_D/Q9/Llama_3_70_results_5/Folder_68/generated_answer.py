def all_odd_ints_inclusive(lst):
    return [lst[i] for i in range(9) if i % 2 != 0 and i < len(lst)]