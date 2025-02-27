def all_even_ints_inclusive(lst):
    even_ints = [x for x in lst[262:747:2]]
    if not even_ints:
        return []
    else:
        return even_ints