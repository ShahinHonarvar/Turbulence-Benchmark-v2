def filter_chars(s):
    for ch in s[10:70]:
        if ch >= 'I' and ch <= 'K':
            s = s.replace(ch, '')
    return s