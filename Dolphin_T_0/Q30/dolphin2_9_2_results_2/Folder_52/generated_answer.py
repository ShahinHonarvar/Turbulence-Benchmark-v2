def insert_before_character(s):
    res = ''
    for i in s:
        if i == 'T':
            res = res + 'V' + i
        else:
            res = res + i
    return res