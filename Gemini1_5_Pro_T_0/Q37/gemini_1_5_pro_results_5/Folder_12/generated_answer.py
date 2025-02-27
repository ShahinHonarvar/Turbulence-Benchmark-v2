def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if i in range(19, 91) and 'F' <= s[i] <= 'h':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s