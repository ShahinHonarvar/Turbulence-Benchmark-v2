def return_n_greatest_chars(s):
    return repr(sorted(set(s)))[-19:][::-1]