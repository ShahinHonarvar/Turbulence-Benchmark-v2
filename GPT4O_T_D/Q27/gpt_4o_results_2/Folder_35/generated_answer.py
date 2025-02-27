def insert_after_index(lst):
    if len(lst) > 100:
        return lst[:101] + [876, 203] + lst[101:]
    else:
        return lst + [876, 203]