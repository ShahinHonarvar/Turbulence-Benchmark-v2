def return_n_smallest_chars(s):
    sorted_chars = sorted(s)[:64]
    sorted_chars.reverse()
    return sorted_chars