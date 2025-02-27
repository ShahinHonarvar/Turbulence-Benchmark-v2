def all_odd_ints_exclusive(lst):
    return [lst[i] for i in range(16, 99) if i in range(len(lst)) and lst[i] % 2 == 1]