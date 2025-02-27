def return_n_smallest_chars(s):
    return sorted(sorted(list(s))[:64], reverse=True)