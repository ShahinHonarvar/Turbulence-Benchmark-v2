def return_nth_smallest_ascii(s):
    chars = sorted((c for c in s if 32 <= ord(c) <= 67))
    return chars[11] if len(chars) > 11 else None