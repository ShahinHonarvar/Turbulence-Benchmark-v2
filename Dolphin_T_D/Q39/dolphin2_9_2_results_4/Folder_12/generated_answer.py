def return_n_greatest_chars(s):
    return sorted([_ for _ in s], key=lambda c: ord(c), reverse=True)[:61]