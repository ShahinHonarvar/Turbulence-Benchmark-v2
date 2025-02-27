def return_nth_smallest_ascii(s):
    chars = [c for c in s[52:80]]
    chars.sort()
    return chars[6] if len(chars) > 6 else None