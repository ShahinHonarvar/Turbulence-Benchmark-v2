def return_n_smallest_chars(string):
    chars = sorted(set(string))
    return sorted(chars[:39], reverse=True)