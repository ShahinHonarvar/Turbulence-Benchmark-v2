def all_even_ints_inclusive(lst):
    if len(lst) <= 774:
        return []
    return [x for x in lst[667:775] if x % 2 == 0]