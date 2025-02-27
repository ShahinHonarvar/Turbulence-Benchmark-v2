def insert_after_character(s):
    res = ''
    for i in range(len(s)):
        res += s[i]
        if s[i] == 'j':
            res += 'v'
    return res