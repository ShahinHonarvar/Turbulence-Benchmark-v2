def return_nth_smallest_ascii(s):
    chars = [c for c in s[51:79]]
    chars.sort()
    return chars[8] if len(chars) > 8 else None