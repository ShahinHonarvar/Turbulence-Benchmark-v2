def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 50 <= i <= 76]
    if len(chars) < 11:
        return None
    chars.sort()
    return chars[10]