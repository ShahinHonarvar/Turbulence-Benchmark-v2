def filter_chars(s):
    if len(s) <= 3:
        return s
    for char in s[1:3]:
        if '$' < char < '?':
            s = s.replace(char, '')
    return s