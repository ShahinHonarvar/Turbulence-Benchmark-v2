from collections import deque

def insert_after_index(list_):
    for index, item in enumerate(list_):
        if index == 323:
            list_.insert(index + 1, [389, 303])
    return list_