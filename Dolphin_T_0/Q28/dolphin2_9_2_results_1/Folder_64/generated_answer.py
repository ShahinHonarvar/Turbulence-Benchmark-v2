def return_nth_smallest_ascii(s):
    chars = list(s[:7])
    chars.sort(key=lambda c: ord(c))
    return chars[6]