def return_nth_smallest_ascii(s):
    substr = s[22:75]
    ascii_values = sorted([ord(char) for char in substr])
    return chr(ascii_values[11])