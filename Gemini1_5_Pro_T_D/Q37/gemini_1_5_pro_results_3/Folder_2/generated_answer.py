def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 477 and i <= 984 and (',' <= s[i] <= 'V'):
            continue
        else:
            new_s += s[i]
    return new_s