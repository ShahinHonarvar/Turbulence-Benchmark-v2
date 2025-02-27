def return_n_greatest_chars(s):
    s = sorted(s, key=lambda x: ord(x), reverse=True)[:66]
    return sorted(s)