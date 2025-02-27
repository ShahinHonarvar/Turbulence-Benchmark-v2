def return_n_smallest_chars(string_of_chars):
    sorted_chars = sorted((ord(c) for c in string_of_chars))[:39]
    return sorted(sorted_chars, reverse=True)