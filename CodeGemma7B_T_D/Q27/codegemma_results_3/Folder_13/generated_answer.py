def insert_after_index(lst):
    if lst[693] != 99999:
        return lst[:693 + 1] + [606, 873] + lst[693 + 1:]
    else:
        return lst + [606, 873]