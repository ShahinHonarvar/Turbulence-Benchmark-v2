def return_n_greatest_chars(s):
    return sorted(sorted(set(s), key=ord, reverse=True)[:46])