def insert_after_index(lst):
    index_to_insert = 73
    element_to_insert = 418.88
    new_length = len(lst) + 1
    new_lst = [None] * new_length
    for i in range(index_to_insert + 1):
        new_lst[i] = lst[i]
    new_lst[index_to_insert + 1] = element_to_insert
    for i in range(index_to_insert + 1, len(lst)):
        new_lst[i + 1] = lst[i]
    return new_lst