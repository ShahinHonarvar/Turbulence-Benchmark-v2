def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 50 <= i <= 75]
    if len(chars) < 7:
        return None
    chars.sort()
    return chars[6]