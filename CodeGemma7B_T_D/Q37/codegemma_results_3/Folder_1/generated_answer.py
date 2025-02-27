def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 41 and i <= 79 and (s[i] >= 'f') and (s[i] <= '|'):
            continue
        new_s += s[i]
    return new_s