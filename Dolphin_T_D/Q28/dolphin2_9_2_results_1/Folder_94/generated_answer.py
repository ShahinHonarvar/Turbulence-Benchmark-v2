def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 6 <= i <= 58]
    ascii_values = [ord(c) for c in chars]
    ascii_values.sort()
    return ascii_values[18]