def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 35 and i <= 89:
            if s[i] >= 'E' and s[i] <= 't':
                continue
            else:
                new_s += s[i]
        else:
            new_s += s[i]
    return new_s