def filter_chars(s):
    for i in range(348, 853):
        if i < len(s) and 'J' <= s[i] <= 'b':
            c = s[i]
            s = s.replace(c, '')
    return s