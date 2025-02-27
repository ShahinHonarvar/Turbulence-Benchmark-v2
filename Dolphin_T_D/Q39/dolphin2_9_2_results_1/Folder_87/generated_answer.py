def return_n_greatest_chars(input_string):
    chars = list(input_string)
    chars.sort(key=lambda x: ord(x), reverse=True)
    return chars[:24]