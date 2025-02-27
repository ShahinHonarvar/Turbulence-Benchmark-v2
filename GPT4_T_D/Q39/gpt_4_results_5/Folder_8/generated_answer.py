def return_n_greatest_chars(s):
    s = ''.join(set(s))
    sorted_chars = sorted(s, key=ord, reverse=True)
    sorted_chars = sorted(sorted_chars[:83])
    return sorted_chars