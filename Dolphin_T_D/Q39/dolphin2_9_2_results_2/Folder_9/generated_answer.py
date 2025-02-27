def return_n_greatest_chars(s):
    return sorted([c for c in s if c in string.ascii_letters][-20:])