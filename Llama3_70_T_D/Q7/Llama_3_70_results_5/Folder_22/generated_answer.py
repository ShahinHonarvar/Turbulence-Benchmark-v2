def all_even_ints_inclusive(lst):
    if len(lst) <= 200:
        return [lst[i] for i in range(40, len(lst)) if i % 2 == 0]
    else:
        return [lst[i] for i in range(40, 201) if i % 2 == 0 and lst[i] % 2 == 0]