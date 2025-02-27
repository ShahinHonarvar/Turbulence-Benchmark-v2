def return_n_greatest_chars(s):
    s = sorted(s, key=ord[::-1])[:60]
    return s