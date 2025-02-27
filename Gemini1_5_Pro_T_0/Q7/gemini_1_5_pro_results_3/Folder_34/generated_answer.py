def all_even_ints_inclusive(lst):
    if len(lst) < 201:
        return []
    else:
        return [i for i in lst[60:201] if i % 2 == 0]