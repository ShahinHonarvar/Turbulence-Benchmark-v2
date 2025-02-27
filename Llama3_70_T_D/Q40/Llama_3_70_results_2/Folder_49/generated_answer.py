def return_n_smallest_chars(s):
    s = ''.join(sorted(s))[:76]
    return sorted(s, reverse=True)