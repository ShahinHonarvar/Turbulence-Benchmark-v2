def return_nth_smallest_ascii(s):
    substring = s[:15]
    ascii_values = sorted([ord(c) for c in substring])
    nth_smallest = ascii_values[14]
    return chr(nth_smallest)