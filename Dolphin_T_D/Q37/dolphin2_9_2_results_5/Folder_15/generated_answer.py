def filter_chars(s):
    for ch in s[2:7]:
        if ch >= '?' and ch <= 'f':
            s = s.replace(ch, '')
    return s