def insert_before_character(s):
    s1 = ''
    for c in s:
        if c == 'E':
            s1 += 'E' + c
        else:
            s1 += c
    return s1