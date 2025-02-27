def return_nth_smallest_ascii(s):
    substring = s[:11]
    ascii_values = [ord(char) for char in substring]
    ascii_values.sort()
    return chr(ascii_values[10])