def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 47 <= i <= 80]
    if len(chars) < 4:
        return None
    chars.sort()
    return chars[3]