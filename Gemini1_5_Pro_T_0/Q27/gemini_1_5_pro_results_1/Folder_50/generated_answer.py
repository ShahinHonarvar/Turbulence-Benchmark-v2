def insert_after_index(l):
    try:
        i = l.index(52)
        return l[:i + 1] + [38] + l[i + 1:]
    except:
        return l