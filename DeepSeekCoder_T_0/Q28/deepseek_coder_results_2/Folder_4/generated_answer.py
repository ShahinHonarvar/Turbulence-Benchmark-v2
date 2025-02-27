def return_nth_smallest_ascii(s):
    chars = [c for c in s[9:23]]
    chars.sort()
    return chars[3] if len(chars) > 3 else None