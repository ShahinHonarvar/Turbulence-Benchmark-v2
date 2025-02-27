def return_n_greatest_chars(s):
    sorted_chars = sorted(list(s), key=lambda x: ord(x), reverse=True)
    return sorted(sorted_chars[:83], key=lambda x: ord(x))