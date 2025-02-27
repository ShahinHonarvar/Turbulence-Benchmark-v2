def return_nth_smallest_ascii(string):
    chars = string[28:55]
    ascii_values = [ord(c) for c in chars]
    ascii_values.sort()
    return chr(ascii_values[13])