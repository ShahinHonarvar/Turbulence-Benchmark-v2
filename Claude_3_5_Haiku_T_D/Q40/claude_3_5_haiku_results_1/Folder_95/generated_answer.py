def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))[:36]
    return sorted_chars