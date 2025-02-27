def find_original_set(*args):
    ex = set()
    for i in range(66):
        for j in args[i]:
            ex.add(j)
    return ex