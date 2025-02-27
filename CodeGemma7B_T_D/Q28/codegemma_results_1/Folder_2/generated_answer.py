def return_nth_smallest_ascii(string_of_chars):
    ascii_values = sorted([ord(char) for char in string_of_chars if 48 <= ord(char) <= 76])
    return chr(ascii_values[4])