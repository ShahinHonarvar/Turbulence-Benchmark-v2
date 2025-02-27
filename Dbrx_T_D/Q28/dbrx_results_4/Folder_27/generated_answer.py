def return_nth_smallest_ascii(s):
    ascii_range = [ord(c) for c in s if 33 <= ord(c) <= 85]
    ascii_range.sort()
    return chr(ascii_range[12]) if len(ascii_range) > 12 else None