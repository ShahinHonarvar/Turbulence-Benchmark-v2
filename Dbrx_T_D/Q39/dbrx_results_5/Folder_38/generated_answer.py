def return_n_greatest_chars(input_string):
    char_list = list(input_string)
    char_list = list(set(char_list))
    char_list.sort(key=ord)
    char_list.reverse()
    return char_list[:45]