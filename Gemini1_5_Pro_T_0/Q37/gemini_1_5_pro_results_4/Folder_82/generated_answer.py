def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 12 <= i <= 25 and 'P' <= s[i] <= 'x':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s