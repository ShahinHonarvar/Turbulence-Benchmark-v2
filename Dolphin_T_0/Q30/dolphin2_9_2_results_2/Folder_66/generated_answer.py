def insert_before_character(s):
    res = ''
    for i in s:
        if i == 'k':
            res += 'k' + i
        else:
            res += i
    return res