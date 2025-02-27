def return_nth_smallest_ascii(s):
    chars = sorted(s[42:60])
    ascii_vals = sorted([ord(c) for c in chars])
    nth_smallest = ascii_vals[16]
    return chr(nth_smallest)