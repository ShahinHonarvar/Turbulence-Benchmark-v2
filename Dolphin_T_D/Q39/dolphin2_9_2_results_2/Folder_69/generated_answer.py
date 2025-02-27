def return_n_greatest_chars(value):
    return sorted([char for char in value], key=lambda x: -ord(x))[:65]