def return_nth_smallest_ascii(s):
    chars = s[38:65]
    sorted_chars = sorted(chars, key=lambda c: ord(c))
    return sorted_chars[13]