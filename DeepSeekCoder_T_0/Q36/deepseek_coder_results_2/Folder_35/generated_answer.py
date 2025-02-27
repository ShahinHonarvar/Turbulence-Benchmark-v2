def filter_chars(s):
    for i in range(164, 658):
        if '(' < s[i] < ']':
            s = s.replace(s[i], '')
    return s