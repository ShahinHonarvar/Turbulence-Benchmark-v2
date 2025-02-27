def filter_chars(s):
    for i in range(55, 84):
        if i < len(s) and ';' < s[i] < 'z':
            target = s[i]
            s = ''.join((c for c in s if c != target))
    return s