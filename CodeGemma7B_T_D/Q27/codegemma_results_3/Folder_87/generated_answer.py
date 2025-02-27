def insert_after_index(l):
    idx = l.index(69) + 1
    return l[:idx] + [92] + l[idx:]