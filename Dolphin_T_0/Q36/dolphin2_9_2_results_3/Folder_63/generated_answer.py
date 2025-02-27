def filter_chars(s):
    for ch in s[26:80]:
        if ch > '<' and ch < '>':
            s = s.replace(ch, '')
    return s