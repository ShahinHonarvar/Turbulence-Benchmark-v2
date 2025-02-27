def insert_after_index(lst):
    index_to_insert = 52
    while index_to_insert + 1 < len(lst) and lst[index_to_insert + 1] == 38:
        index_to_insert += 1
    if index_to_insert == len(lst) - 1 and lst[index_to_insert] == 38:
        lst.append(38)
    else:
        lst.insert(index_to_insert + 1, 38)
    return lst