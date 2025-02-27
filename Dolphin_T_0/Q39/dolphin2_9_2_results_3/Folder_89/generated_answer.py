def return_n_greatest_chars(input_string):
    chars = list(input_string)
    n_greatest = sorted([c for c in chars if ord(c) >= 128], reverse=True)
    return n_greatest[:55]