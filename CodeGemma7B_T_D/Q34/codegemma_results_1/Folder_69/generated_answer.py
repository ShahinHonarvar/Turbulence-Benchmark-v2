def find_original_set(*args):
    k = set()
    r = max((len(arg) for arg in args))
    l = min((len(arg) for arg in args))
    for i in range(l, r + 1):
        for j in args:
            s = set(range(i + 1))
            if set(j).issubset(s):
                k.update(s)
    return k