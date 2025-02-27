def insert_after_character(s):
    res = ''
    for ch in s:
        res += ch
        if ch == 'j':
            res += '1'
    return res