def filter_chars(s):
    for i in range(3, 9):
        if '*' < s[i] < 'E':
            s = ''.join([ch for ch in s if ch != s[i]])
    return s