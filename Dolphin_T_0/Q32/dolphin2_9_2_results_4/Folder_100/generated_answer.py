def insert_after_character(s):
    res = ''
    for i in s:
        res += i + ' ' if i == '0' else i
    return res