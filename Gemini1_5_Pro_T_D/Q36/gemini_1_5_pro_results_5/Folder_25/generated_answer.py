def filter_chars(s):
    temp = ''
    for i in range(len(s)):
        if i > 24 and i < 37 and (s[i] > 'A') and (s[i] < 'h'):
            temp = s[i]
            s = s.replace(s[i], '')
    return s