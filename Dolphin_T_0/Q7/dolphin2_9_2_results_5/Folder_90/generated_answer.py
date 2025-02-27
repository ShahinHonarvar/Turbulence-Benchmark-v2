def all_even_ints_inclusive(lst):
    even_ints = [x for x in lst[262:747] if x % 2 == 0]
    if not even_ints:
        return []
    return even_ints