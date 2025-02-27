def return_n_smallest_chars(chars):
    n = 47
    sorted_chars = sorted(chars)
    return sorted_chars[:n][::-1]