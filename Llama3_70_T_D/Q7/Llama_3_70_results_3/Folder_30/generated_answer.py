def all_even_ints_inclusive(lst):
    return [lst[i] for i in range(55, 99) if i < len(lst) and lst[i] % 2 == 0]