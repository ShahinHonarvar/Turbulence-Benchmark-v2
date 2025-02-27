def insert_after_index(lst):
    new_list = lst
    try:
        new_list.insert(lst.index(761) + 1, 925)
    except ValueError:
        print('Index not found.')
    return new_list