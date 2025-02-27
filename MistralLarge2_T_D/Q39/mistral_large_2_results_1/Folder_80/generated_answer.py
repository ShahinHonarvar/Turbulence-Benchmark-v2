def return_n_greatest_chars(s):
    return sorted([char for char in s], key=lambda c: -ord(c))[:35]