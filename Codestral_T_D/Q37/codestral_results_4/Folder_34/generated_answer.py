def filter_chars(s):
    for ch in s[54:63]:
        if ')' <= ch <= '9':
            s = s.replace(ch, '')
    return s