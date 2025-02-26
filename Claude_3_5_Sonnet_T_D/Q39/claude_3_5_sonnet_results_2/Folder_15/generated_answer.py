def return_n_greatest_chars(input_string):
    char_list = list(set(input_string))
    char_list.sort(reverse=True)
    return sorted(char_list[:57])