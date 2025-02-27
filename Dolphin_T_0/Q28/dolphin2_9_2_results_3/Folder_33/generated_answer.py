def return_nth_smallest_ascii(string):
    filtered_chars = string[22:75]
    ascii_values = [ord(char) for char in filtered_chars]
    ascii_values.sort()
    return chr(ascii_values[11])