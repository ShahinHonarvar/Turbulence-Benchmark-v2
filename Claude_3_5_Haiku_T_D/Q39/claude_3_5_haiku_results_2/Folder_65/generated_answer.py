def return_n_greatest_chars(s):
    chars = list(set(s))
    chars.sort(reverse=True)
    return chars[:27]