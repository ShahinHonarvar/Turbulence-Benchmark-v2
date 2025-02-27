def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('The function requires 87 distinct set arguments')
    result = set()
    for subset in args:
        result |= subset
    return result