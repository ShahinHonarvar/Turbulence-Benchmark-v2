def find_original_set(a):
    b = set()
    for x in a:
        b = b.union(x)
    return b