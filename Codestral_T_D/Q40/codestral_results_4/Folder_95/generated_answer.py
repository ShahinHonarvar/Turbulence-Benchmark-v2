def return_n_smallest_chars(s):
    return sorted(s[:min(36, len(s))])