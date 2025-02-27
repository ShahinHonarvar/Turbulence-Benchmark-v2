def insert_before_character(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'Y':
            s.insert(i, '4')
    return ''.join(s)