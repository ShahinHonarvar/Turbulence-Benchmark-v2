def return_n_greatest_chars(s):
    return list(sorted(s, key=ord)[-76:])