def filter_chars(s):
    s = list(s)
    for i in range(49, 56):
        if i < len(s):
            c = s[i]
            if 'I' < c < 'a':
                s = [x for x in s if x != c]
    return ''.join(s)