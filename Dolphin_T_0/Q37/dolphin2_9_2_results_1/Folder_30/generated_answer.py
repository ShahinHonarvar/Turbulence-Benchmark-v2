def filter_chars(s):
    for ch in s:
        if 41 <= s.index(ch) <= 64 and ch >= 'K' and (ch <= ']'):
            s = s.replace(ch, '')
    return s