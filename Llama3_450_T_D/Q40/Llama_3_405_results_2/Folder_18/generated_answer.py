def return_n_smallest_chars(s):
    sorted_s = sorted(s)
    n_smallest_chars = sorted_s[:52]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars