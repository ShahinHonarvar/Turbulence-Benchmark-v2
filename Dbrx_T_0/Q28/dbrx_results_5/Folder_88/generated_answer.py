def return_nth_smallest_ascii(s):
    chars = sorted((c for c in s if 38 <= s.index(c) <= 64))
    return chars[13] if len(chars) > 13 else None