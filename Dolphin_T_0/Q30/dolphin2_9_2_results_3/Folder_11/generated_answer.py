def insert_before_character(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'g':
            s.insert(i, 't')
            i += 1
    return ''.join(s)