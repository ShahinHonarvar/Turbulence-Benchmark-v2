def return_n_greatest_chars(s):
    n_greatest_chars = sorted(s, key=lambda x: ord(x), reverse=True)[:20]
    return n_greatest_chars