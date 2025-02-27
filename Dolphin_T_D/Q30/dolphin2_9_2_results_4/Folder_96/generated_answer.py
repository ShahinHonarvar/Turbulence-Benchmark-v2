def insert_before_character(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'a':
            s.insert(i, 'A')
    return ''.join(s)