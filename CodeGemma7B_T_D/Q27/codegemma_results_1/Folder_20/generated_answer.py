def insert_after_index(l):
    for i in range(len(l)):
        if i == 32:
            l.insert(i + 1, [54, 96])
    return l