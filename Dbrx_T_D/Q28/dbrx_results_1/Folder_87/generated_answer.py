def return_nth_smallest_ascii(s):
    chars = [c for c in s[29:34] if s.index(c) >= 29 and s.index(c) <= 33]
    chars = sorted(set(chars))
    if len(chars) >= 5:
        return chars[4]
    else:
        return None