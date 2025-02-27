def all_even_ints_inclusive(lst):
    if len(lst) < 64:
        return []
    result = [i for i in lst[14:65] if i % 2 == 0]
    return result