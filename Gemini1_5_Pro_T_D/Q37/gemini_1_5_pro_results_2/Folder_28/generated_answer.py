def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i >= 20 and i <= 79 and (ord(s[i]) >= ord('!')) and (ord(s[i]) <= ord('T')):
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s