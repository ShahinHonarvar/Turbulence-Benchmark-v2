def all_even_ints_exclusive(lst):
    return [lst[i] for i in range(90, 200) if i < len(lst) and lst[i] % 2 == 0]