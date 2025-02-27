def return_nth_smallest_ascii(s):
    sliced_string = s[35:53]
    ascii_values = sorted([ord(c) for c in sliced_string])
    return chr(ascii_values[9])