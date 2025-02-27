def return_n_greatest_chars(char_string):
    char_list = [ord(c) for c in char_string]
    char_list.sort(reverse=True)
    return char_list[:45]