def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for i, c in enumerate(s) if 25 <= i <= 45]
    ascii_values.sort()
    return chr(ascii_values[10])