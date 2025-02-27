def return_n_smallest_chars(string):
    unique_chars = list(set(string))
    unique_chars.sort()
    return unique_chars[:17]