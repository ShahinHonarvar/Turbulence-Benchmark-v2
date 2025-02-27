def filter_chars(s):
    new_s = ''
    for i in range(0, 63):
        new_s += s[i]
    for i in range(63, 89):
        if s[i] > '*' and s[i] < 'w':
            s = s.replace(s[i], '')
    for i in range(89, len(s)):
        new_s += s[i]
    return new_s