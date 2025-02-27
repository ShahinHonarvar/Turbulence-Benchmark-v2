def return_nth_smallest_ascii(s):
    chars = [c for c in s if 62 <= ord(c) <= 83]
    chars.sort(key=ord)
    return chars[8] if len(chars) > 8 else None