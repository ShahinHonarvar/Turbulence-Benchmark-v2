def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(50, 77)]
    ascii_values = [ord(c) for c in chars]
    ascii_values.sort()
    return chr(ascii_values[10])