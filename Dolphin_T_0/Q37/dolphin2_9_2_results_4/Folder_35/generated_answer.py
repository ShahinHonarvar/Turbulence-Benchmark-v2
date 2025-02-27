def filter_chars(s):
    chars = []
    for i in range(155, 404):
        if '(' <= s[i] <= ']':
            chars.append(s[i])
    for char in chars:
        s = s.replace(char, '')
    return s