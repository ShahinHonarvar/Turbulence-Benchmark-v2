def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 38 <= i <= 54 and ':' <= s[i] <= 'r':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s