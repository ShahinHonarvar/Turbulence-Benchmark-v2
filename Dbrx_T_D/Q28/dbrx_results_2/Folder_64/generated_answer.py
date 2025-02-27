def return_nth_smallest_ascii(s):
    chars = [c for c in set(s) if s.index(c) <= 6]
    chars.sort(key=ord)
    return chars[6] if len(chars) > 6 else None