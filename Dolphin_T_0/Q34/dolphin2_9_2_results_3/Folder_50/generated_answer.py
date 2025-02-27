def find_original_set(*args):
    result = set(*args[0])
    for i in range(1, 99):
        result |= set(*args[i])
    return result