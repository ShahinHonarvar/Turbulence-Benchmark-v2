def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 25 and i <= 97 and (s[i] >= 'm') and (s[i] <= 'w'):
            continue
        else:
            new_s += s[i]
    return new_s