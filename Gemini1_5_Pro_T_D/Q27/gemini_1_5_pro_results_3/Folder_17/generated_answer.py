def insert_after_index(l):
    for i in range(len(l)):
        if l[i] == 94:
            return l[:i + 1] + [93] + l[i + 1:]
    return l