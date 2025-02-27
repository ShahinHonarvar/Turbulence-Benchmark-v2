import sys

def insert_at_index(lst):
    lst = lst[:4] + [7] + lst[4:]
    return lst