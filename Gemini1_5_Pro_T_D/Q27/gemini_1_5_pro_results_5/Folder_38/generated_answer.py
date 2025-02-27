def insert_after_index(l):
    i = l.index(89)
    return l[:i + 1] + [86] + l[i + 1:]