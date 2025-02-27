def find_original_set(*args):
    original_set = None
    min_length = float('inf')
    for s in args:
        if len(s) < min_length:
            min_length = len(s)
            original_set = s
    return original_set