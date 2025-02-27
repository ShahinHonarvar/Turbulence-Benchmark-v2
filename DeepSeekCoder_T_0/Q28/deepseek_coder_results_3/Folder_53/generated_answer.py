def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 40 <= i <= 60]
    if len(chars) < 19:
        return None
    chars.sort()
    return chars[18]