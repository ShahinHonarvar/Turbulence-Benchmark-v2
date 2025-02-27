def return_nth_smallest_ascii(s):
    chars = sorted(s[14:36])
    ascii_values = [ord(c) for c in chars]
    return chr(sorted(ascii_values)[10])