def return_n_greatest_chars(s):
    greatest_chars = sorted(s, reverse=True)[:82]
    return sorted(greatest_chars)