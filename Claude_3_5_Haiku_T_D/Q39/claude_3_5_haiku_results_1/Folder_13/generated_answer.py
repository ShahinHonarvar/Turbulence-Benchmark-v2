def return_n_greatest_chars(s):
    return sorted(list(s))[-31:] if len(s) >= 31 else sorted(list(s))