def return_n_greatest_chars(unique_char_string):
    unique_char_string = sorted(sorted(unique_char_string), key=ord, reverse=True)
    return unique_char_string[:40]