def return_n_smallest_chars(s):
    return sorted(sorted(list(s))[:7], reverse=True)