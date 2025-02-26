def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), key=ord, reverse=True)[:43]
    return sorted(sorted_chars)