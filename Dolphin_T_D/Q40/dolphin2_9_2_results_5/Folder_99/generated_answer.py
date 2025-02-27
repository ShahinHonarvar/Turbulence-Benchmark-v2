def return_n_smallest_chars(s):
    chars = sorted(s)[:35]
    return sorted(chars, reverse=True)