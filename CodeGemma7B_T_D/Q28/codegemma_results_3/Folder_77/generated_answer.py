def return_nth_smallest_ascii(string):
    ascii_values = []
    for char in string:
        if 63 <= string.index(char) <= 76:
            ascii_values.append(ord(char))
    ascii_values.sort()
    return chr(ascii_values[13])