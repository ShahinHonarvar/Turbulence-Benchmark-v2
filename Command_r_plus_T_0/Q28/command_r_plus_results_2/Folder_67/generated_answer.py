def return_nth_smallest_ascii(s):
    sub_s = s[60:84]
    ascii_values = [ord(char) for char in sub_s]
    ascii_values.sort()
    return chr(ascii_values[13])