def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 27 and i <= 85 and (s[i] >= 'c') and (s[i] <= 'i'):
            continue
        else:
            new_s += s[i]
    return new_s