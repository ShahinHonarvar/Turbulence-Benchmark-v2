def return_n_greatest_chars(char_list):
    return sorted([char for char in char_list], key=ord)[-83:]