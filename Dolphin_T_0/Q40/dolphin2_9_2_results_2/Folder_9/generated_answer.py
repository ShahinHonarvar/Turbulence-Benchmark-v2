def return_n_smallest_chars(s):
    return sorted(s, key=lambda x: ASCII(x))[:20]