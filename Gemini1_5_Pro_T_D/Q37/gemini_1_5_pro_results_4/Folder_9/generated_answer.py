def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 38 <= i <= 99 and 'A' <= s[i] <= 'Q':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s