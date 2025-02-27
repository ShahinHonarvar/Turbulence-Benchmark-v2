def insert_after_index(l):
    if len(l) > 28:
        return l[:29] + [20] + l[29:]
    else:
        return l