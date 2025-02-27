def insert_after_index(lst, index=24):
    if index == len(lst) - 1:
        return lst + [98, 22]
    else:
        return lst[:index + 1] + [98, 22] + lst[index + 1:]