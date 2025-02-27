def return_n_greatest_chars(char_str):
    return sorted(char_str, key=ord)[:66]