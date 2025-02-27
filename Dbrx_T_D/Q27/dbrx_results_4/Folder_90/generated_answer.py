def insert_after_index(lst):
    index_761 = next((i for i, x in enumerate(lst) if x == 761), None)
    if index_761 is not None:
        return lst[:index_761 + 1] + [925] + lst[index_761 + 1:]
    else:
        return lst