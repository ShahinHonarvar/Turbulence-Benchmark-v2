def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 19 <= i <= 90 and 'F' <= s[i] <= 'h':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s