def insert_after_character(s):
    res = ''
    for i in s:
        res += i + (i == ' ' and '5')
    return res