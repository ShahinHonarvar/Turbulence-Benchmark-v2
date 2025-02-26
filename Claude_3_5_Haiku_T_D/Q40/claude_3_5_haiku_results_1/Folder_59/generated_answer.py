def return_n_smallest_chars(s):
    return sorted(sorted(set(s))[:13], reverse=True)