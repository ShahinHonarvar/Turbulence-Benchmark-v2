def all_even_ints_inclusive(lst):
    if len(lst) < 23:
        return []
    sublist = lst[22:51]
    return [num for num in sublist if num % 2 == 0]