def return_n_greatest_chars(s):
    s = ''.join(sorted(s, reverse=True))
    return [char for i, char in enumerate(s) if i < 54]