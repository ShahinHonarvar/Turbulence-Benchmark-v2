def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 55 <= i < 66:
            if s[i] > 'f' and s[i] < '|':
                s = s.replace(s[i], '')
    return s