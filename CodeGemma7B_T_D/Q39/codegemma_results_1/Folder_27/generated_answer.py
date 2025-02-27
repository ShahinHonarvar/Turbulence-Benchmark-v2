def return_n_greatest_chars(char_list):
    return sorted(sorted(char_list), key=ord, reverse=True)[:82]