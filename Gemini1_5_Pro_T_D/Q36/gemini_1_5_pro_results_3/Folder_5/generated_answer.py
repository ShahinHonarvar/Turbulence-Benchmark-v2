def filter_chars(s):
    temp = ''
    for i in range(len(s)):
        if 55 < i < 66 and 'f' < s[i] < '|':
            temp = s[i]
            s = s.replace(temp, '')
    return s