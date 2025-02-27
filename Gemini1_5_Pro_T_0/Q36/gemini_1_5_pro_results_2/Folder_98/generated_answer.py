def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 4 < i < 8 and '1' < s[i] < 'J':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s