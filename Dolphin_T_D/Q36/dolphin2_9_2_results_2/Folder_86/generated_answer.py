def filter_chars(s):
    for i in range(672, 710):
        if s[i] > 'X' and s[i] < '}':
            s = s.replace(s[i], '')
    return s