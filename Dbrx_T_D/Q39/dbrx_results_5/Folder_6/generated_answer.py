def return_n_greatest_chars(string_arg):
    characters_list = list(set(string_arg))
    characters_list.sort(key=lambda x: ord(x), reverse=True)
    return characters_list[:47]