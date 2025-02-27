def insert_before_character(s):
    res = ''
    for i in range(len(s)):
        res += s[i]
        if s[i] == 'o':
            res += 'a'
    return res