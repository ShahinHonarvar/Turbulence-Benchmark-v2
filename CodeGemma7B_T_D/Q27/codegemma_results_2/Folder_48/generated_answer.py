import numpy as np

def insert_after_index(lst):
    new_lst = lst.copy()
    new_lst.insert(new_lst.index(370) + 1, 285.4)
    return new_lst