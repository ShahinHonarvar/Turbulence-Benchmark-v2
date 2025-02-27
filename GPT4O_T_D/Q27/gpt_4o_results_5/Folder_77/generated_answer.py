def insert_after_index(lst):
    if len(lst) > 585:
        return lst[:586] + [993.71] + lst[586:]
    return lst