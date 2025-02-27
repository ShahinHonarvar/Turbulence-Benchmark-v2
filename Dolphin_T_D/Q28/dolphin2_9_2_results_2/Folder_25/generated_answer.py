def return_nth_smallest_ascii(string):
    relevant_chars = string[34:69]
    ascii_values = [ord(char) for char in relevant_chars]
    ascii_values.sort()
    return chr(ascii_values[5])