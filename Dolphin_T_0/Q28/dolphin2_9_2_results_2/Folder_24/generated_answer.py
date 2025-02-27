def return_nth_smallest_ascii(s):
    valid_chars = s[34:82]
    ascii_values = [ord(c) for c in valid_chars]
    nth_smallest = sorted(ascii_values)[11]
    return chr(nth_smallest)