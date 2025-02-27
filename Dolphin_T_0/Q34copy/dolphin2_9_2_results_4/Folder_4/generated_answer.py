def find_original_set(*args):
    s = set()
    for i in range(len(args)):
        for j in args[i]:
            s.add(j)
    return s