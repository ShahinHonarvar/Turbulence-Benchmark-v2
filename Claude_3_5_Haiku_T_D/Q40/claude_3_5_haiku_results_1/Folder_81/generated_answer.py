def return_n_smallest_chars(s):
    sorted_chars = sorted(list(set(s)))[:64]
    return sorted_chars