def filter_chars(string):
    s = list(string)
    for i in range(343, 665):
        if '%' < s[i] < 'U':
            remove(s, i)
    return ''.join(s)