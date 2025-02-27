def insert_after_character(s):
    res = ''
    for i in s:
        res += i
        if i == 'w':
            res += 'n'
    return res