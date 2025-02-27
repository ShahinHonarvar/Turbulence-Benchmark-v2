def filter_chars(s):
    for i in range(299, 418):
        if i >= len(s):
            break
        if s[i] > '9' and s[i] < 'P':
            s = s.replace(s[i], '')
    return s