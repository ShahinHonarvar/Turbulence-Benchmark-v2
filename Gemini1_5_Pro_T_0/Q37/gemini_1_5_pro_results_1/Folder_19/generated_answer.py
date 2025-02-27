def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 35 <= i <= 89 and 'E' <= s[i] <= 't':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s