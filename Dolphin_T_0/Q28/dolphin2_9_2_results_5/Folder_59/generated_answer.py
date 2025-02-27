def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 0 <= i <= 11]
    chars.sort(key=ord)
    return chars[11]