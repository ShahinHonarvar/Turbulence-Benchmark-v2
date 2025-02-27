def return_n_greatest_chars(char_str):
    sorted_list = sorted(set(char_str), key=ord, reverse=True)
    return sorted_list[:66]