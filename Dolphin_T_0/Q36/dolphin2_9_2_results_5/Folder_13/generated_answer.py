def filter_chars(s):
    for char in range(323, 526):
        if s[char] > ')' and s[char] < 'O':
            s = s.replace(s[char], '')
    return s