def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 46 <= i <= 82]
    ascii_values = [c for c in chars]
    ascii_values = [ord(c) for c in ascii_values]
    ascii_values.sort()
    return chr(ascii_values[15])