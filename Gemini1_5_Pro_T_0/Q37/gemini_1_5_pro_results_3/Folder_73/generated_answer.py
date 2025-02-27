def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 22 <= i <= 85 and '7' <= s[i] <= 'e':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s