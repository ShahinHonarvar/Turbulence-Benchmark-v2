def return_nth_smallest_ascii(s):
    chars = sorted((c for i, c in enumerate(s) if 36 <= i <= 79))
    return chars[11] if len(chars) > 11 else None