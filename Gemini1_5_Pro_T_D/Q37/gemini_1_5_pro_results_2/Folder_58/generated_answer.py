def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 503 <= i <= 753 and '9' <= s[i] <= 'w':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s