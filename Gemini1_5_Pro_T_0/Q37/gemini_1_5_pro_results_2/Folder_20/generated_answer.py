def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i in range(25, 98) and 'm' <= s[i] <= 'w':
            continue
        new_s += s[i]
    return new_s