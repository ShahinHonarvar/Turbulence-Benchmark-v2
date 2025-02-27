def filter_chars(s):
    for ch in s[14:75]:
        if ch > '9' and ch < 'K':
            s = s.replace(ch, '')
    return s