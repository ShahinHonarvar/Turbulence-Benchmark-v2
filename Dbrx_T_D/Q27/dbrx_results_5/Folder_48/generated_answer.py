def insert_after_index(lst):
    index_to_insert = 370
    index_to_check = index_to_insert + 1
    if index_to_check < len(lst):
        new_list = lst[:index_to_check] + [285.4] + lst[index_to_check:]
    else:
        new_list = lst[:]
        new_list.append(285.4)
    return new_list