def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 15 <= i <= 55 and 'W' <= s[i] <= '{':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s