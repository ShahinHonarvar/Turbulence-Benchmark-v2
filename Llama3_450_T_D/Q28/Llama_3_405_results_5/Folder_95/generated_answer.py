def return_nth_smallest_ascii(s):
    chars_between_indices = s[1:47]
    ascii_values = [ord(char) for char in chars_between_indices]
    unique_ascii_values = sorted(set(ascii_values))
    return chr(unique_ascii_values[12])