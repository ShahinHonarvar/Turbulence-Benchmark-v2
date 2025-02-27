def return_nth_smallest_ascii(s):
    chars = [c for c in s if 47 <= ord(c) <= 70]
    chars.sort(key=ord)
    return chars[13] if len(chars) > 14 else None