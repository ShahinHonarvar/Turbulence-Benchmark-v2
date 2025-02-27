def return_n_smallest_chars(s):
    return sorted(s, key=lambda x: (x < s[:76], x))[::-1][:76]