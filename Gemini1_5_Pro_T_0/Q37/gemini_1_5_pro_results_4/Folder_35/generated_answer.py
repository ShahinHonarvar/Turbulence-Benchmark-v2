def filter_chars(s):
    for i in range(155, 404):
        if i < len(s) and '(' <= s[i] <= ']':
            c = s[i]
            s = s.replace(c, '')
    return s