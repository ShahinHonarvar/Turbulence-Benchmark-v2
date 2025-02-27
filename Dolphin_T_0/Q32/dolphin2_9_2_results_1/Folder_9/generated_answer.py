def insert_after_character(s):
    res = ''
    for i in s:
        if i == 'e':
            res += i + 'E'
        else:
            res += i
    return res