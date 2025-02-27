def filter_chars(s):
    for char in sorted(set(s[54:63])):
        if ')' <= char <= '9':
            s = s.replace(char, '')
    return s