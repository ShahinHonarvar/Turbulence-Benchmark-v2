def return_nth_smallest_ascii(s):
    chars_between_indices = s[8:66]
    ascii_values = sorted((ord(c) for c in chars_between_indices))
    return chr(ascii_values[5])