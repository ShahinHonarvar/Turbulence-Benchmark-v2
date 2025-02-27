def all_even_ints_exclusive(lst):
    if len(lst) < 94:
        return []
    return [i for i in lst[92:94] if i % 2 == 0]