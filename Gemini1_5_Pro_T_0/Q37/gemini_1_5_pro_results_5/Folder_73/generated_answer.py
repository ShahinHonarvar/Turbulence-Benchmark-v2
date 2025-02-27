def filter_chars(s):
    filtered_chars = ''
    for i in range(22, 86):
        if i < len(s) and '7' <= s[i] <= 'e':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s