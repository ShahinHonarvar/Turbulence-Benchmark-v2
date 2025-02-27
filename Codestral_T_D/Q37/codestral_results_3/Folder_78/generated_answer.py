def filter_chars(s):
    for char in sorted(s[75:100]):
        if '8' <= char <= 'e':
            s = s.replace(char, '')
    return s