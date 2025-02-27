def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string if 0 <= string.index(char) <= 5]
    ascii_values.sort()
    return chr(ascii_values[5]) if len(ascii_values) > 5 else None