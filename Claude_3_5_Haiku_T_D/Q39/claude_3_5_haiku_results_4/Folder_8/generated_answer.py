def return_n_greatest_chars(s):
    return sorted(list(s))[-83:] if len(s) >= 83 else sorted(list(s))