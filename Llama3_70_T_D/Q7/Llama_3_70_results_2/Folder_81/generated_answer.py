def all_even_ints_inclusive(lst):
    return [lst[i] for i in range(10, 101) if i < len(lst) and lst[i] % 2 == 0]