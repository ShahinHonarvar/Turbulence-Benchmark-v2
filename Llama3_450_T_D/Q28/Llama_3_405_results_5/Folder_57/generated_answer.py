def return_nth_smallest_ascii(s):
    chars = sorted(s[17:35])
    return min(chars, key=lambda c: ord(c) - ord(min(chars)) >= 17 and ord(c))