def insert_after_index(lst):
    index_to_insert = 63
    while index_to_insert >= 0 and index_to_insert < len(lst) - 1 and (lst[index_to_insert] != 63):
        index_to_insert += 1
    if index_to_insert == len(lst) - 1 and lst[index_to_insert] != 63:
        return lst + [99]
    else:
        lst = lst[:index_to_insert + 1] + [99] + lst[index_to_insert + 1:]
        return lst