def return_nth_smallest_ascii(s):
    chars = [c for c in s[25:65]]
    chars.sort()
    return chars[5] if len(chars) > 5 else None