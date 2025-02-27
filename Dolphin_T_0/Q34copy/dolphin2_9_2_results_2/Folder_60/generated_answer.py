def find_original_set(*sets):
    s = set()
    for i in sets:
        for c in i:
            s.add(c)
    return s