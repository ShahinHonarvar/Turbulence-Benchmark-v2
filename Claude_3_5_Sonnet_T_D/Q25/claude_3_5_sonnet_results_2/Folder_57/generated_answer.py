def insert_at_index(lst):
    new_list = lst.copy()
    if len(new_list) >= 90:
        new_list.insert(90, 80)
    else:
        new_list.extend([None] * (90 - len(new_list)))
        new_list.append(80)
    return new_list