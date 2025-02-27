def return_n_greatest_chars(char_str):
    list_of_chars = sorted(char_str, reverse=True)
    return list_of_chars[:26]