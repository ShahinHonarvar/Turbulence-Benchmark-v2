def filter_chars(s):
    s = s[:43] + ''.join((ch for ch in s[43:59] if ch not in '6789:;<=>?@[\\\\]^_`abcdefghijklmnopqrstuvwxyz')) + s[59:]
    return s