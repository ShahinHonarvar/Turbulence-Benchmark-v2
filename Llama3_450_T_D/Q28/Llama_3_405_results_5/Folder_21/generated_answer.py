def return_nth_smallest_ascii(s):
    chars_between_indices = s[8:66]
    ascii_values = [ord(c) for c in chars_between_indices]
    ascii_values.sort()
    return chr(ascii_values[5])