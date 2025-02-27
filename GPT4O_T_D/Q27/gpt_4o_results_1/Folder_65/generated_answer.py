def insert_after_index(lst):
    if len(lst) > 70:
        return lst[:71] + [185.43] + lst[71:]
    return lst