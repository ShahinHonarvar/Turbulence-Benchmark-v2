def return_nth_smallest_ascii(s):
    chars = s[20:81]
    ascii_values = [ord(c) for c in chars]
    return chr(ascii_values[10])