def return_nth_smallest_ascii(string):
    list_chars = string[17:84]
    ascii_values = [ord(char) for char in list_chars]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_char = list_chars[sorted_ascii_values.index(sorted_ascii_values[4])]
    return nth_smallest_char