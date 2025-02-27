def find_original_set(*args):
    result = set()
    for input_set in args:
        result |= input_set
    return result