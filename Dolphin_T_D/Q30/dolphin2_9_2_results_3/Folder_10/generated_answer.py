def insert_before_character(s):
    res = ''
    for i in range(len(s)):
        if s[i] == 'j':
            res += 'v'
        res += s[i]
    return res