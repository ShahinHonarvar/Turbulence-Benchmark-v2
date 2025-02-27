def insert_before_character(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'U':
            s.insert(i, 'q')
    return ''.join(s)