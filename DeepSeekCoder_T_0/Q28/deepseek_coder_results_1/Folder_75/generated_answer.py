def return_nth_smallest_ascii(s):
    chars = [c for c in s[62:84]]
    chars.sort()
    return chars[8] if len(chars) > 8 else None