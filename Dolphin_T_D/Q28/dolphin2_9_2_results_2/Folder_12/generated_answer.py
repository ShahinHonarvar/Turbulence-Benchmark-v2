def return_nth_smallest_ascii(s):
    chars = s[3:27]
    ascii_values = [ord(c) for c in chars]
    ascii_values.sort()
    return chr(ascii_values[4])