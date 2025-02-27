def return_n_greatest_chars(input_string):
    unique_chars = list(set(input_string))
    unique_chars.sort(key=lambda char: ord(char), reverse=True)
    return unique_chars[:8]