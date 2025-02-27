def return_n_smallest_chars(s):
    unique_chars = sorted(set(s), key=s.index)
    n_smallest_chars = sorted(unique_chars[:75], reverse=True)
    return n_smallest_chars