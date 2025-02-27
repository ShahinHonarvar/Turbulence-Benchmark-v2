def return_nth_smallest_ascii(s):
    chars = [c for c in s if 52 <= ord(c) <= 79]
    chars.sort(key=ord)
    return chars[6] if len(chars) > 6 else None