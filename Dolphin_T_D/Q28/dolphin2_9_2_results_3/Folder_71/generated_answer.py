def return_nth_smallest_ascii(s):
    chars = s[5:83]
    ascii_values = [ord(c) for c in chars]
    nth_smallest = sorted(ascii_values)[15]
    return chr(nth_smallest)