def return_nth_smallest_ascii(str):
    ascii_values = sorted([ord(char) for char in str[47:71]])
    return chr(ascii_values[13])