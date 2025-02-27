def return_n_greatest_chars(s):
    s = ''.join(sorted(s, reverse=True))
    return list(s[:32])