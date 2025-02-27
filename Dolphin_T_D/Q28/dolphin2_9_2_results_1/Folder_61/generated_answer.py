def return_nth_smallest_ascii(s):
    chars = sorted(s[:10], key=lambda c: ord(c))
    return chars[9]