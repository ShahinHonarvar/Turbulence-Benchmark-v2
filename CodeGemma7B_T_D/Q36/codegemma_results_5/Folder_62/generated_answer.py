def filter_chars(s):
    return ''.join((ch for ch in s if ch not in set(s[63:89]) or (ch > '*' and ch < 'w')))