def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i > 15 and i < 85 and (s[i] > 'I') and (s[i] < 'M'):
            continue
        new_s += s[i]
    return new_s