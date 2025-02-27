def return_nth_smallest_ascii(s):
    chars_in_range = sorted(s[18:46])
    ascii_values = [ord(c) for c in chars_in_range]
    seventh_smallest_ascii = sorted(set(ascii_values))[6]
    return chr(seventh_smallest_ascii)