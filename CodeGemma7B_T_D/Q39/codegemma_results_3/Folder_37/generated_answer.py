def return_n_greatest_chars(char_list):
    sorted_list = sorted(char_list, key=ord, reverse=True)[:26]
    return sorted_list