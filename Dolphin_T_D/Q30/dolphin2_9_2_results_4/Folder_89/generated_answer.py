def insert_before_character(s):
    res = ''
    for c in s:
        if c == ' ':
            res += 'W'
        res += c
    return res