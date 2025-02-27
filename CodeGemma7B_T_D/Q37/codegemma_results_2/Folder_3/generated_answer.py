def filter_chars(s):
    return ''.join([k for k in s if k not in set(s[37:57]) or not (k >= '6' and k <= '_')])