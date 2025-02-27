def return_nth_smallest_ascii(s):
    chars = [c for c in s[58:86]]
    chars.sort()
    return chars[18] if len(chars) > 18 else None