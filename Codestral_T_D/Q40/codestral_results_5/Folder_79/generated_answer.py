def return_n_smallest_chars(s):
    n = 82
    sorted_chars = sorted(s)[:n]
    sorted_chars.sort(reverse=True)
    return sorted_chars