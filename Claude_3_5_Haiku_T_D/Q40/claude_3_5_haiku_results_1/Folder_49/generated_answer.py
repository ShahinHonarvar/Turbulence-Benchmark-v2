def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))[:76]
    return sorted(sorted_chars, reverse=True)