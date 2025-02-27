def return_nth_smallest_ascii(s):
    chars = list(s[:5])
    chars.sort(key=lambda c: ord(c))
    return chars[3]