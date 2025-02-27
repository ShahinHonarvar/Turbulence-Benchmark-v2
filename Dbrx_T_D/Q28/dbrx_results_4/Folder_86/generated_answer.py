def return_nth_smallest_ascii(s):
    chars = [c for c in s[44:70] if 32 <= ord(c) <= 122]
    chars.sort(key=ord)
    return chars[14] if len(chars) > 14 else None