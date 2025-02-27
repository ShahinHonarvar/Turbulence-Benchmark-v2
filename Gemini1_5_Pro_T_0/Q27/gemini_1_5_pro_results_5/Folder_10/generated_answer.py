def insert_after_index(l):
    i = l.index(56) + 1
    return l[:i] + [54] + l[i:]