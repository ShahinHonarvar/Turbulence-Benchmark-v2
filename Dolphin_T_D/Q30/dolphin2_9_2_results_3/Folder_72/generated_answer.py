def insert_before_character(s):
    res = ''
    for c in s:
        if c == 'O':
            res += 'd' + c
        else:
            res += c
    return res