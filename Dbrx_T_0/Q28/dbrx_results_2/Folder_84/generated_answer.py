def return_nth_smallest_ascii(s):
    ascii_range = [ord(c) for c in s if 52 <= s.index(c) <= 79]
    ascii_range.sort()
    return chr(ascii_range[6]) if len(ascii_range) >= 7 else None