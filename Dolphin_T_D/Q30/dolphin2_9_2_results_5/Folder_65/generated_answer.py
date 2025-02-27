def insert_before_character(s):
    res = ''
    for i in range(len(s)):
        if s[i] == '6':
            res += '9' + s[i]
        else:
            res += s[i]
    return res