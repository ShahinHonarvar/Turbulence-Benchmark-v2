def return_n_greatest_chars(input_string):
    n = 39
    chars = list(input_string)
    chars.sort(key=lambda x: -ord(x))
    return chars[:n]