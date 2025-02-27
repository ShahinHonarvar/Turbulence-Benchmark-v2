def all_even_ints_exclusive(lst):
    if len(lst) < 100:
        return []
    result = [i for i in lst[86:99] if i % 2 == 0]
    return result