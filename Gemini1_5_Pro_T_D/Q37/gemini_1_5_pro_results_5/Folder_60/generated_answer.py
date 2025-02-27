def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if 12 <= i <= 77 and ':' <= s[i] <= 'L':
            filtered_chars += s[i]
    for c in filtered_chars:
        s = s.replace(c, '')
    return s