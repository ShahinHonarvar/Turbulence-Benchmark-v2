def all_odd_ints_inclusive(lst):
    return [lst[i] for i in range(10) if i in range(len(lst)) and lst[i] % 2 != 0]