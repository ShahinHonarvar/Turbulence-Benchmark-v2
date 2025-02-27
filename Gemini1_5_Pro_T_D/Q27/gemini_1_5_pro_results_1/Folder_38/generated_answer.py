def insert_after_index(l):
    for i in range(len(l)):
        if l[i] == 89:
            return l[:i + 1] + [86] + l[i + 1:]
    return l