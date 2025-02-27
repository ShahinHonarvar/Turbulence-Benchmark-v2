def filter_chars(s):
    for ch in s[21:43]:
        if ch >= '+' and ch <= '8':
            s = s.replace(ch, '')
    return s