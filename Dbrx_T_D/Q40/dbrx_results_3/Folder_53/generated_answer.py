def return_n_smallest_chars(string_arg):
    char_list = [char for char in string_arg if char != ' ']
    char_list.sort(key=lambda x: ord(x))
    return char_list[:19]