def return_n_greatest_chars(s):
    return sorted(max(s, key=lambda x: ord(x), cutoff=14))[:14]