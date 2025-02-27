def insert_after_index(lst):
    return [x for i, x in enumerate(lst) if i != 990] + [[905, 742]] + [x for i, x in enumerate(lst) if i == 990 and lst[i] not in [905, 742]]