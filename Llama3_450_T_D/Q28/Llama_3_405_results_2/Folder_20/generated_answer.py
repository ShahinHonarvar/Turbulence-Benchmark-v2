def return_nth_smallest_ascii(s):
    chars_between_indices = sorted([c for i, c in enumerate(s) if 25 <= i <= 64])
    ascii_values = sorted([ord(c) for c in chars_between_indices])
    sixth_smallest_ascii = ascii_values[5]
    return chr(sixth_smallest_ascii)