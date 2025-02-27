def return_n_greatest_chars(char_str):
    result = sorted(char_str, key=ord, reverse=True)[:38]
    return result