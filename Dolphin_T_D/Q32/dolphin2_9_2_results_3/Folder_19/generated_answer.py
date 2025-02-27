def insert_after_character(s):
    res = ''
    for c in s:
        res += c
        if c == '5':
            res += 'h'
    return res