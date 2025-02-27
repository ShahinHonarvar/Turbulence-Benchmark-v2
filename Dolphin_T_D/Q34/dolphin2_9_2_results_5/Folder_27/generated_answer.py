def find_original_set(*sets):
    s = sets[0]
    for i in range(1, len(sets)):
        s = s | sets[i]
    return s