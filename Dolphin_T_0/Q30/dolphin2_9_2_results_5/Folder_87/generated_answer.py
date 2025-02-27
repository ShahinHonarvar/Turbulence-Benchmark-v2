def insert_before_character(s):
    res = ''
    for i in range(len(s)):
        if s[i] == 'm':
            res += 'N' + s[i]
        else:
            res += s[i]
    return res