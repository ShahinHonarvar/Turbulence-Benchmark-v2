def insert_at_index(lst):
    if len(lst) >= 990:
        return lst[:990] + [[905, 742]] + lst[990:]
    else:
        return lst + [[905, 742]]