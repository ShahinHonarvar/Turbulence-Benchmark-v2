def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 29 and i <= 97 and (s[i] >= '-') and (s[i] <= 'n'):
            continue
        else:
            new_s += s[i]
    return new_s