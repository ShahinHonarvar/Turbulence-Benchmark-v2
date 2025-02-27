def return_n_greatest_chars(s):
    s = sorted(s, key=ord)
    return s[len(s) - 82:]