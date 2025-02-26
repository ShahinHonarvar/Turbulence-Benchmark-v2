def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), key=ord, reverse=True)[:24]
    return sorted(sorted_chars)