def return_n_greatest_chars(string_arg):
    char_list = list(string_arg)
    char_list = [ord(char) for char in char_list]
    char_list = sorted(char_list, reverse=True)
    char_list = [chr(char) for char in char_list]
    return char_list[:7]