def filter_chars(s):
    for i in range(63, 89):
        if '*' < s[i] < 'w':
            s = ''.join((ch for ch in s if ch != s[i]))
    return s