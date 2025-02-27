def return_nth_smallest_ascii(s):
    chars = sorted(s[:19])
    ascii_values = sorted([ord(c) for c in chars])
    nth_smallest = ascii_values[12]
    return chr(nth_smallest)