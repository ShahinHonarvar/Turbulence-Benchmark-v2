def return_nth_smallest_ascii(str):
    ascii_values = sorted([ord(char) for char in str[5:83]], key=int)
    return chr(ascii_values[15])