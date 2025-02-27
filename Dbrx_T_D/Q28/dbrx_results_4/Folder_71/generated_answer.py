def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string if 5 <= string.index(c) <= 82]
    ascii_values.sort()
    return ascii_values[15] if len(ascii_values) > 15 else None