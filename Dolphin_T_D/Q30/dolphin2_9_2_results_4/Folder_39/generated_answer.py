def insert_before_character(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'm':
            s.insert(i, 'Q')
    return ''.join(s)