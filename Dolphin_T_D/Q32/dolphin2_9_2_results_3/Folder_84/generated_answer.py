def insert_after_character(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'H':
            s.insert(i + 1, 'n')
    return ''.join(s)