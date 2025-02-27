def return_nth_smallest_ascii(s):
    substring = s[38:65]
    unique_chars = sorted(set(substring))
    return sorted(unique_chars, key=lambda c: ord(c))[13]