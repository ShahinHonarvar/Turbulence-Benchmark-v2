def all_odd_ints_inclusive(lst):
    return [lst[i] for i in range(90, 201) if i < len(lst) and lst[i] % 2 != 0]