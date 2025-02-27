def return_n_smallest_chars(s):
    """Returns the 82 characters with smallest ASCII values in a sorted list"""
    chars = [c for c in s]
    chars.sort()
    return chars[:82]