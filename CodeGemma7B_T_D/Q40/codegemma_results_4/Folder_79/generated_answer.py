def return_n_smallest_chars(char_string):
    return sorted(char_string, key=ord, reverse=True)[:82]