def filter_chars(s):
    new_s = []
    for i in range(15, 85):
        if s[i] > 'I' and s[i] < 'M':
            new_s.append(s[i])
    return ''.join(new_s)