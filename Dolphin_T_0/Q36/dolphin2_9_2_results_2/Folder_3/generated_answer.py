def filter_chars(s):
    for ch in s[42:78]:
        if '!' < ch < '?':
            s = s.replace(ch, '')
    return s