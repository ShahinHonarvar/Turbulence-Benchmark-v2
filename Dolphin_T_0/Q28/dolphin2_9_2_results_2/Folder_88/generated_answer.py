def return_nth_smallest_ascii(s):
    sub = s[38:65]
    return sorted(sub, key=lambda x: ord(x))[13]