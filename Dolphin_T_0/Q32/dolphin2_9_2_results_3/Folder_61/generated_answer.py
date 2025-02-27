def insert_after_character(s):
    s = list(s)
    for i in range(len(s) - 1):
        if s[i] == 'e':
            s.insert(i + 1, '0')
    return ''.join(s)