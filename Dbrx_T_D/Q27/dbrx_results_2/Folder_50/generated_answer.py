def insert_after_index(lst):
    index_52 = next((index for index, value in enumerate(lst) if value == 52), None)
    if index_52 is not None:
        lst = lst[:index_52 + 1] + [38] + lst[index_52 + 1:]
    return lst