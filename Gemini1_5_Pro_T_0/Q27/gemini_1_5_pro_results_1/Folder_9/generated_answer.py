def insert_after_index(l):
    i = l.index(66) + 1
    return l[:i] + [45] + l[i:]