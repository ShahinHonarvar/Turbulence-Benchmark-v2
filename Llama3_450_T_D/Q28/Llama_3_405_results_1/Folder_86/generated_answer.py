def return_nth_smallest_ascii(s):
    chars_between_indices = s[44:70]
    ascii_values = [ord(c) for c in chars_between_indices]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[14])