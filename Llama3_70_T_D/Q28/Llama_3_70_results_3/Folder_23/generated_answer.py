def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(29, 48)]
    ascii_values = sorted([ord(c) for c in chars])
    return chr(ascii_values[6])