def return_n_smallest_chars(s):
    chars_sorted = sorted(set(s))[:38]
    return sorted(chars_sorted, reverse=True)