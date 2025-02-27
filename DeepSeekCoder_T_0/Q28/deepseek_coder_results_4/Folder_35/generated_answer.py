def return_nth_smallest_ascii(s):
    chars = sorted(s[50:76])
    return chars[6] if len(chars) > 6 else None