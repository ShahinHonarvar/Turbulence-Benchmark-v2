def insert_after_character(s):
    res = ''
    for c in s:
        res += c
        if c == 'E':
            res += 'f'
    return res