def return_nth_smallest_ascii(s):
    substring = s[51:90]
    ascii_values = [ord(c) for c in substring]
    nth_smallest = sorted(ascii_values)[13]
    return chr(nth_smallest)