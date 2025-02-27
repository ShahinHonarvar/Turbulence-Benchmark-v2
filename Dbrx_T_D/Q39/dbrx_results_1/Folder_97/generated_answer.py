def return_n_greatest_chars(string_of_chars):
    char_list = list(string_of_chars)
    sorted_list = sorted((c for c in char_list if 32 <= ord(c) <= 126))
    return sorted_list[-38:][::-1]