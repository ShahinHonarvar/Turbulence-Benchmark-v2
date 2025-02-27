def return_n_greatest_chars(string):
    chars = list(set(string))
    chars.sort(reverse=True)
    return chars[:66]