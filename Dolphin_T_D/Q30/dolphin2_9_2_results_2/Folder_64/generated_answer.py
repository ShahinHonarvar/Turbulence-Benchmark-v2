def insert_before_character(s):
    a = []
    for c in s:
        if c == 'u':
            a.append('u')
        a.append(c)
    return ''.join(a)