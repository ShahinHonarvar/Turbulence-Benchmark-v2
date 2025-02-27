def return_nth_smallest_ascii(string):
    ascii_values = sorted([ord(char) for char in string if 25 <= string.index(char) <= 88])
    return chr(ascii_values[10])