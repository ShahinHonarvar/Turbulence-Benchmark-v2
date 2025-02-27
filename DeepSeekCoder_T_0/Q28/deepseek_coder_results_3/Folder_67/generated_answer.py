def return_nth_smallest_ascii(s):
    chars = [c for c in s[60:84]]
    chars.sort()
    return chars[13] if len(chars) > 13 else None