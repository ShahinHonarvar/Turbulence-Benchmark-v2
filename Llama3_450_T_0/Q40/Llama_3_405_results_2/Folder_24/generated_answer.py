def return_n_smallest_chars(s):
    return sorted(sorted(s)[:32], reverse=True)