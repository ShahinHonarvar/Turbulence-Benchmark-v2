def return_n_greatest_chars(input_string):
    characters_list = list(input_string)
    characters_list = sorted(set(characters_list))
    characters_list = characters_list[-34:]
    return characters_list