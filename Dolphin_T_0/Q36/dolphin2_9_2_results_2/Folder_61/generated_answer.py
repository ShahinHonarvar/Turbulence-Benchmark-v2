def filter_chars(s):
    for i in range(3, 9):
        if '*' < s[i] < 'E':
            s = ''.join([c for c in s if c != s[i]])
    return s