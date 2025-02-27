def return_nth_smallest_ascii(s):
    chars = sorted((c for c in s if 25 <= ord(c) <= 64))
    return chars[5] if len(chars) > 5 else None