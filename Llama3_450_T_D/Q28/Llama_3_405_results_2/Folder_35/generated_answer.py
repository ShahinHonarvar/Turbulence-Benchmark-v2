def return_nth_smallest_ascii(s):
    chars = sorted(set(s[50:76]))
    if len(chars) < 7:
        return None
    else:
        return min(sorted(chars), key=lambda x: ord(x), default=None)