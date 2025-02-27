def return_n_smallest_chars(s):
    sorted_chars = sorted(list(s))
    return sorted(sorted_chars[:min(49, len(sorted_chars))], reverse=True)