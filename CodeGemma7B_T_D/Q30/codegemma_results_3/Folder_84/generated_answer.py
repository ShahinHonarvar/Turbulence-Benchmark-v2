def insert_before_character(s):
    r = ''
    for c in s:
        if c == 'H':
            r = r + 'nH'
        else:
            r = r + c
    return r