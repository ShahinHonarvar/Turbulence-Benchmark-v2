def return_nth_smallest_ascii(string):
    chars = string[0:88]
    ascii_values = [ord(char) for char in chars]
    ascii_values.sort()
    return chr(ascii_values[13])