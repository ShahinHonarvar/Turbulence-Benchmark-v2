def insert_after_character(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'E':
            s.insert(i + 1, 'e')
    return ''.join(s)