def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 24 and i < 37 and (s[i] > 'A') and (s[i] < 'h'):
            continue
        new_s += s[i]
    return new_s