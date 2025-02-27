def filter_chars(s):
    s = list(s)
    for i in range(10, 53):
        if '@' <= s[i] <= 'T':
            s = [x for x in s if x not in s[i]]
    return ''.join(s)