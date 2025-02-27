def return_n_greatest_chars(string_arg):
    ascii_chars = [char for char in string_arg if ord(char) >= ord('!') and ord(char) <= ord('~')]
    sorted_chars = sorted(ascii_chars, key=ord, reverse=True)[:17]
    return sorted(sorted_chars, key=ord)