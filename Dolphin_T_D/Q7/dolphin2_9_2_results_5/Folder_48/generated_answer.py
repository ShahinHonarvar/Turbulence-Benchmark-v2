def all_even_ints_inclusive(lst):
    output = [i for i in lst[533:606] if i % 2 == 0]
    if not output:
        return []
    else:
        return output