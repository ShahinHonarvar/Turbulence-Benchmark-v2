def filter_chars(s):
    for ch in s[12:46]:
        if '!' < ch < 'A':
            s = s.replace(ch, '')
    return s