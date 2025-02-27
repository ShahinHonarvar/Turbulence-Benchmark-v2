def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 38 <= i <= 82]
    chars.sort(key=ord)
    return chars[19] if len(chars) > 19 else None