def filter_chars(s):
    for i in range(22, 25):
        if '5' < s[i] < '}':
            while s.count(s[i]) > 0:
                s = s.replace(s[i], '')
    return s