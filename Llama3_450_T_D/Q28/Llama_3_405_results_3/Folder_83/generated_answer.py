def return_nth_smallest_ascii(s):
    chars = sorted(s[30:71])
    return min(chars, key=lambda x: (x > min(chars), x)) if len(chars) < 15 else sorted(chars, key=lambda x: x)[14]