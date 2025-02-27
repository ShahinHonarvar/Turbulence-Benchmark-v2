def filter_chars(s):
    for i in range(78, 81):
        if 'S' < s[i] < '[':
            s = ''.join([c for c in s if c != s[i]])
    return s