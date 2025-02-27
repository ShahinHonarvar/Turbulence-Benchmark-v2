def all_pos_ints_inclusive(lst):
    result = [i for i in lst[30:201] if i > 0]
    if not result:
        result = []
    return result