def return_n_greatest_chars(string):
    return sorted(list(string), key=lambda k: -ord(k))[:64]