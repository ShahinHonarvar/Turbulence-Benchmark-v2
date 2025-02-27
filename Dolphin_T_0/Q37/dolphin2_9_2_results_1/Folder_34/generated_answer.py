def filter_chars(s):
    for c in s[54:63]:
        if c >= ')' and c <= '9':
            s = s.replace(c, '')
    return s