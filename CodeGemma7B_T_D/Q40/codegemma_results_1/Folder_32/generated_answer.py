def return_n_smallest_chars(str_arg):
    list_of_ascii = [ord(char) for char in str_arg]
    list_of_ascii.sort()
    return [chr(ascii_value) for ascii_value in list_of_ascii[:8]]