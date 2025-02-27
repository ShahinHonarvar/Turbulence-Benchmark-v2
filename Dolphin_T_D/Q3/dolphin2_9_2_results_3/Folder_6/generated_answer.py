def all_pos_ints_inclusive(data):
    subset = [i for i in data[10:67] if i > 0]
    return subset if subset else []