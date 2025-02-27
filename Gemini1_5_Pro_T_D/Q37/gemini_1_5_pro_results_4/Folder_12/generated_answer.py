def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i >= 19 and i <= 90 and (ord(s[i]) >= ord('F')) and (ord(s[i]) <= ord('h')):
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s