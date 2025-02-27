def return_nth_smallest_ascii(s):
    chars = sorted(s[8:66])
    return min(chars, key=lambda c: (ord(c), chars.index(c) if ord(c) in [ord(x) for x in chars[:5]] else float('inf')))