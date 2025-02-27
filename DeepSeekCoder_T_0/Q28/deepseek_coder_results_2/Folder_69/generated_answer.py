def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 67 <= i <= 77]
    chars.sort()
    return chars[6] if len(chars) > 6 else None