def return_nth_smallest_ascii(string):
    ascii_values = sorted([ord(c) for c in string[60:84] if ord(c) >= 65 and ord(c) <= 90])
    return chr(ascii_values[13])