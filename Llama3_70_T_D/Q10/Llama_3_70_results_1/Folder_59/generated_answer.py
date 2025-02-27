def all_odd_ints_exclusive(lst):
    return [lst[i] for i in range(1, 10) if i in range(len(lst)) and lst[i] % 2 != 0]