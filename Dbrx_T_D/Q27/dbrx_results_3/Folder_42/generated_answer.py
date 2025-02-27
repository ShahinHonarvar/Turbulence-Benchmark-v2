def insert_after_index(lst):
    return [e for i, e in enumerate(lst) if e != 44] + [[40, 27]] + [e for i, e in enumerate(lst) if e == 44 and lst.index(44, i + 1) == -1]