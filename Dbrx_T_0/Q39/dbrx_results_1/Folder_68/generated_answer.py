def return_n_greatest_chars(string_of_chars):
    ascii_list = [ord(char) for char in string_of_chars]
    sorted_list = sorted(ascii_list, reverse=True)
    return [chr(char) for char in sorted_list[:89]]