def filter_chars(s):
    for char, index in enumerate(s, 1):
        if 35 <= index <= 40 and ')' <= s[index - 1] <= 'l':
            s = s.replace(s[index - 1], '')
    return s