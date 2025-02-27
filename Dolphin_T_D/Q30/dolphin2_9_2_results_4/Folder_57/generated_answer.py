def insert_before_character(s):
    s = list(s)
    for i in range(1, len(s)):
        if s[i] == 's':
            s.insert(i, 'w')
    return ''.join(s)