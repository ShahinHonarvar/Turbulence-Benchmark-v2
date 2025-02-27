def filter_chars(s):
    for ch in s[69:87]:
        if ch > '#' and ch < 'L':
            s = s.replace(ch, '')
    return s