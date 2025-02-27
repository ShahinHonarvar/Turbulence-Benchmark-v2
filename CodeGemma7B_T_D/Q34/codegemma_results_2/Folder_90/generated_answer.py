def find_original_set(allsets):
    current_set = set()
    for s in allsets:
        current_set |= s
    return current_set