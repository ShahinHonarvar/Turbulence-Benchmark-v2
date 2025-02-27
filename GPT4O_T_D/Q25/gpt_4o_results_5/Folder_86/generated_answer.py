def insert_at_index(lst):
    if len(lst) >= 990:
        lst.insert(990, [905, 742])
    else:
        lst.append([905, 742])
    return lst