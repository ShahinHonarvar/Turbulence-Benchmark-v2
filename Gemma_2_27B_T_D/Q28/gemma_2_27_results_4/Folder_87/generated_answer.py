def return_nth_smallest_ascii(s):
    sub_string = s[29:34]
    ascii_values = sorted([ord(char) for char in sub_string])
    return chr(ascii_values[4])