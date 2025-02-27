def return_nth_smallest_ascii(s):
    sub_str = s[37:60]
    ascii_values = [ord(char) for char in sub_str]
    ascii_values.sort()
    return chr(ascii_values[5])