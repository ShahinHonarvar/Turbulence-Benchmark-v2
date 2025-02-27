def find_original_set(*args):
    s = set()
    for i in args:
        if len(i) != 0:
            for j in i:
                if j not in s:
                    s.add(j)
    return s