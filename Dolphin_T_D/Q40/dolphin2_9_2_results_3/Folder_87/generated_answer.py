def return_n_smallest_chars(s):
    """Create a list of 24 characters with the smallest ASCII values from a string of distinct characters"""
    return_list = sorted([char for char in s], key=lambda x: ord(x))[:24]
    return return_list