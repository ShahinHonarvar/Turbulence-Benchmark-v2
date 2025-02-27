def return_nth_smallest_ascii(s):
    chars = sorted(s[25:46])
    ascii_values = [ord(c) for c in chars]
    unique_ascii_values = sorted(set(ascii_values))
    return chr(unique_ascii_values[10])