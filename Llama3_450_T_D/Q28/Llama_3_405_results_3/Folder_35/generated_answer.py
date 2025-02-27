def return_nth_smallest_ascii(s):
    chars = sorted(s[50:76])
    ascii_values = [ord(c) for c in chars]
    seventh_smallest = ascii_values[6]
    return chr(seventh_smallest)