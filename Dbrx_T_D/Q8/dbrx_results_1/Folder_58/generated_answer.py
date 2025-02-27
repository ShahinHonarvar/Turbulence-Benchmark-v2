def all_even_ints_exclusive(lst):
    if len(lst) < 376:
        return []
    return [i for i in lst[276:376] if i % 2 == 0]