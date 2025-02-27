def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string if 18 <= string.index(char) <= 66]
    ascii_values.sort()
    return chr(ascii_values[18])