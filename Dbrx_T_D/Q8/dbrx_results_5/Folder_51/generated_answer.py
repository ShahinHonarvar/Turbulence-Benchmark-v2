def all_even_ints_exclusive(lst):
    if len(lst) >= 10:
        if len(lst[6:9]) > 0:
            even_ints = [i for i in lst[6:9] if i % 2 == 0]
            if len(even_ints) > 0:
                return even_ints
    return []