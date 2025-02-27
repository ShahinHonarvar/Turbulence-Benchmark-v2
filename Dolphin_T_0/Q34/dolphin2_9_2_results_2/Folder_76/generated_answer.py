def find_original_set(*args):
    result = set()
    for container in args:
        result |= container
    return result