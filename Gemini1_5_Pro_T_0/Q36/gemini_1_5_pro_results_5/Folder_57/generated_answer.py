def filter_chars(s):
    for i in range(70, 74):
        if i < len(s) and 'A' < s[i] < 'U':
            c = s[i]
            s = ''.join((x for x in s if x != c))
    return s