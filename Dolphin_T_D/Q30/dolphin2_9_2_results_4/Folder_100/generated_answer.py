def insert_before_character(s):
    s = list(s)
    for i in range(len(s) - 1):
        if s[i + 1] == '0':
            s.insert(i + 1, ' ')
    return ''.join(s)