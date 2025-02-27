def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 60 <= i <= 83]
    chars.sort(key=lambda c: ord(c))
    return chars[13]