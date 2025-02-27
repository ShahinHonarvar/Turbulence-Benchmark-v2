def all_pos_ints_exclusive(lst):
    return [int for int in lst[1:-1] if int > 0]