def return_nth_smallest_ascii(s):
    chars = sorted(s[:11])
    return min(chars, key=lambda x: (ord(x), chars.index(x)), default=None) if len(chars) >= 11 else None