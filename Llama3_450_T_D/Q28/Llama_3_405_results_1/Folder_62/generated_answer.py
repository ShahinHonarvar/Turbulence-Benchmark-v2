def return_nth_smallest_ascii(s):
    characters = sorted(set(s[51:79]))
    ascii_values = sorted([ord(c) for c in characters])
    return chr(ascii_values[8])