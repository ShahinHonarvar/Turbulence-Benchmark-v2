def return_n_greatest_chars(string_of_chars):
    char_list = list(string_of_chars)
    sorted_chars = sorted(char_list, key=ord)[:32]
    return sorted_chars