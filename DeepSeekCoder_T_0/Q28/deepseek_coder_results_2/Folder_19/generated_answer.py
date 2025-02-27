def return_nth_smallest_ascii(s):
    chars = [c for c in s[0:19]]
    chars.sort()
    return chars[12] if len(chars) > 12 else None