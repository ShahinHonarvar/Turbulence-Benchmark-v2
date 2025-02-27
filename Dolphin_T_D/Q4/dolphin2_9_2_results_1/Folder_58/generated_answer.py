def all_pos_ints_exclusive(lst):
    result = [i for i in lst[276:376] if i > 0]
    if not result:
        return []
    return result