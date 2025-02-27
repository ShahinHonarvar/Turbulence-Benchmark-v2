def insert_before_character(s):
    res = ''
    for i in s:
        if i == 'i':
            res += 'I'
            res += i
        else:
            res += i
    return res