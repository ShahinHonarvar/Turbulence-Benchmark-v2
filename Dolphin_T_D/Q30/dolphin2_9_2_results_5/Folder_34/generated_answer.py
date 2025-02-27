def insert_before_character(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'A':
            s.insert(i, 'a')
    return ''.join(s)