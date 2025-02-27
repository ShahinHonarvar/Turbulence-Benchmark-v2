def insert_after_character(s):
    res = ''
    for i in range(len(s)):
        if s[i] == 'Y':
            res = res + s[i] + '4'
        else:
            res += s[i]
    return res