def return_nth_smallest_ascii(s):
    chars = sorted(s)[32:68]
    return chars[11] if len(chars) > 11 else None