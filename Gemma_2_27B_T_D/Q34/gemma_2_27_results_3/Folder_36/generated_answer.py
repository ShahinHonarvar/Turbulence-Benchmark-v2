def find_original_set(*sets):
    result = sets[0]
    for i in range(1, 714):
        result |= sets[i]
    return result