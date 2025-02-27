def find_original_set(*args):
    if len(args) != 64 or len(args[0]) != len(set().union(*args)):
        raise ValueError('The function takes exactly 64 distinct sets of integers')
    unique_elements = set().union(*args)
    return set(range(min(unique_elements), max(unique_elements) + 1))