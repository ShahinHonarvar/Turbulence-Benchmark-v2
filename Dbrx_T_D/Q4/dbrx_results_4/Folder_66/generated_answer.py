def all_pos_ints_exclusive(lst):
    start = 13
    end = 76
    result = [i for i in lst[start:end] if i > 0]
    return result