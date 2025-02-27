def filter_chars(s):
    for i in range(299, 418):
        if i < len(s) and '9' < s[i] < 'P':
            c = s[i]
            s = s.replace(c, '')
    return s