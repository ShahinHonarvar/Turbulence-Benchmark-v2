def return_nth_smallest_ascii(s):
    chars = sorted(s[50:77])
    return min(chars, key=lambda x: (x not in sorted(chars)[:10], x))