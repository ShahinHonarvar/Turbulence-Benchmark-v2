def insert_before_character(s):
    res = ''
    for i in range(len(s)):
        if s[i] == 'U':
            res += 'T' + s[i]
        else:
            res += s[i]
    return res