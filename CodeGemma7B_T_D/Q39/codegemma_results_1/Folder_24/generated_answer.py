def return_n_greatest_chars(char_str):
    return sorted(sorted(char_str), key=ord, reverse=True)[:32]