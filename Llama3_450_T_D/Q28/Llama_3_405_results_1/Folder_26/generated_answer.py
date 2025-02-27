def return_nth_smallest_ascii(s):
    chars = sorted(s[1:37])
    return sorted(chars, key=lambda x: ord(x))[14]