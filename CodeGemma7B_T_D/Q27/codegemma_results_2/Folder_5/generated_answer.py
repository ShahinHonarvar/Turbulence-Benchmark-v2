def insert_after_index(l):
    for i in range(len(l)):
        if i == 99:
            l.insert(i + 1, 15)
    return l