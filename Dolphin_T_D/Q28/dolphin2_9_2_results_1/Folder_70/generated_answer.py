def return_nth_smallest_ascii(s):
    chars = s[28:55]
    ascii_vals = [ord(c) for c in chars]
    nth_smallest = sorted(ascii_vals)[13]
    return chr(nth_smallest)