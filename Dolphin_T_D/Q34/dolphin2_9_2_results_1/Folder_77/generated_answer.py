def find_original_set(*sets):
    s = None
    for set in sets:
        if s is None:
            s = set
        else:
            s = s | set
    return s