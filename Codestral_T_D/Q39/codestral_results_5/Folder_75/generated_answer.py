def return_n_greatest_chars(char_string):
    sorted_chars = sorted(char_string, reverse=True)
    return sorted_chars[:2]