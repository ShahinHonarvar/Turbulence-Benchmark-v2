def return_nth_smallest_ascii(s):
    sub_string = s[21:60]
    ascii_values = [ord(char) for char in sub_string]
    ascii_values.sort()
    return chr(ascii_values[10])