def all_even_ints_inclusive(lst):
    result = [i for i in lst[262:747:2]]
    if result:
        return result
    else:
        return []