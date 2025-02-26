def return_n_smallest_chars(string):
    sorted_chars = sorted(string)[:36]
    return sorted(sorted_chars, reverse=True)