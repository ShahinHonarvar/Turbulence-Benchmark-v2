def all_pos_ints_exclusive(lst):
    start = 111
    end = 473
    return [num for num in lst[start:end] if num > 0]