def return_n_greatest_chars(input_string):
    chars = list(input_string)
    chars.sort(reverse=True)
    return chars[:20]