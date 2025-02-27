def find_original_set(*args):
    s, found = (set(), set())
    for a in ars:
        if not a.issubset(s):
            s |= a
        else:
            found.add(a)
    return (s, found)