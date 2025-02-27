def insert_after_character(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'U':
            s.insert(i + 1, 'q')
    return ''.join(s)