def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 60 <= i <= 88]
    if len(chars) < 7:
        return None
    chars.sort()
    return chars[6]