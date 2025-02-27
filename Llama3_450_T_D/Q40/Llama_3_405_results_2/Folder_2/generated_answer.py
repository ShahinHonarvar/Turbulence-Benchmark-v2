def return_n_smallest_chars(s):
    unique_chars = sorted(set(s))
    return sorted(unique_chars * (48 // len(unique_chars) + 1))[:48]