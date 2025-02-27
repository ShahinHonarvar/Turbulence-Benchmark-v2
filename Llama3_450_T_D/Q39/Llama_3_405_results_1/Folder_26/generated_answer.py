def return_n_greatest_chars(s):
    s = sorted(s, key=lambda x: ord(x), reverse=True)[:43]
    return sorted(s)