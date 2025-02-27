def insert_after_index(lst):
    if 990 > len(lst):
        return lst + [905, 742]
    else:
        return lst[:990] + [905, 742] + lst[990:]