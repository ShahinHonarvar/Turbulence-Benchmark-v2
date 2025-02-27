def return_nth_smallest_ascii(s):
    sub = s[38:65]
    sorted_chars = sorted(sub, key=lambda x: ord(x))
    return sorted_chars[13]