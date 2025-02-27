def insert_before_character(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'u':
            s.insert(i, 'U')
    return ''.join(s)