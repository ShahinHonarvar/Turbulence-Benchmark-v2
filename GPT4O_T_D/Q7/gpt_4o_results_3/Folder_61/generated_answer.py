def all_even_ints_inclusive(lst):
    if len(lst) <= 7:
        return []
    result = [x for x in lst[7:8] if x % 2 == 0]
    return result