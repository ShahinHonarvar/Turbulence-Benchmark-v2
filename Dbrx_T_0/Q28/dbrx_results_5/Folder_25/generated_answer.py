def return_nth_smallest_ascii(s):
    chars = sorted((c for c in s if 34 <= s.index(c) <= 68))
    return chars[5] if len(chars) > 5 else None