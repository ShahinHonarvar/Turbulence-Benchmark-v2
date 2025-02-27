def filter_chars(s):
    for i in range(18, 38):
        ch = s[i]
        if ')' < ch < 'P':
            s = s.replace(ch, '')
    return s