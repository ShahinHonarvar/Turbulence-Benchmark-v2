def return_n_smallest_chars(s):
    sorted_chars = sorted(s)[:16]
    return sorted_chars[::-1]