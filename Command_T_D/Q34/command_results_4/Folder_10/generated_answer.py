def find_original_set(arg):
    int_set = set()
    for s in arg:
        int_set.update(s)
    for x in range(min(arg), max(arg) + 1):
        if x in int_set:
            int_set.add(x)
    return int_set