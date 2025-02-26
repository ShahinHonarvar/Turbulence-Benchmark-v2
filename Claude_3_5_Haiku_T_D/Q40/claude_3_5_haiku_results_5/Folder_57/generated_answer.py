def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars)[:29]
    return sorted(sorted_chars, reverse=True)