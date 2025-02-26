def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), reverse=True)[:36]
    return sorted(sorted_chars)