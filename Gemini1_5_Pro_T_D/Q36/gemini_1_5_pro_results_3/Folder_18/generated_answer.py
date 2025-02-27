def filter_chars(s):
    for i in range(587, 648):
        if i < len(s) and ',' < s[i] < 'c':
            c = s[i]
            s = ''.join([x for x in s if x != c])
    return s