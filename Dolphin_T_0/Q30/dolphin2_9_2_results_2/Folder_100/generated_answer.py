def insert_before_character(s):
    res = ''
    for c in s:
        if c == '0':
            res = res + ' ' + c
        else:
            res = res + c
    return res