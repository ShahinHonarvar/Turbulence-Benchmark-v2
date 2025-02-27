def insert_after_index(lst):
    if 693 in lst:
        index = lst.index(693) + 1
        return lst[:index] + [606, 873] + lst[index:]
    else:
        return lst