def return_nth_smallest_ascii(s):
    chars = sorted(s[1:32])
    ascii_vals = [ord(c) for c in chars]
    sixth_smallest = sorted(ascii_vals)[5]
    return chr(sixth_smallest)