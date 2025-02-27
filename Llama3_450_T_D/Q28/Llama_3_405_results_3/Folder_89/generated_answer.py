def return_nth_smallest_ascii(s):
    sliced_string = s[24:72]
    ascii_values = [ord(c) for c in sliced_string]
    ascii_values.sort()
    return chr(ascii_values[7])