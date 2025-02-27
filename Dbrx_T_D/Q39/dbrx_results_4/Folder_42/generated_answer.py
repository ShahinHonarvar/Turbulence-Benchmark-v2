def return_n_greatest_chars(s):
    chars = sorted(s, key=ord, reverse=True)[:59]
    return ''.join(chars)