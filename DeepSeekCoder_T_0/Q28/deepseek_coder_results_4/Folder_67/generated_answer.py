def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 60 <= i <= 83]
    if len(chars) < 14:
        return None
    chars.sort()
    return chars[13]