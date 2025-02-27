def insert_before_character(s):
    res = ''
    for i in range(len(s)):
        if s[i] == '5':
            res += 'R'
        res += s[i]
    return res