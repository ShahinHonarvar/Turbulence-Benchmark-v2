def return_n_smallest_chars(s):
    sorted_chars = sorted(list(set(s)))[:60]
    return sorted_chars