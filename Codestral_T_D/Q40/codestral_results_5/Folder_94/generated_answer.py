def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    n_smallest_chars = sorted_chars[:87]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars