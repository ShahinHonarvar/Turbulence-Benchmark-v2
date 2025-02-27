def filter_chars(s):
    for i in range(324, 526):
        if ')' < s[i] < 'O':
            s = s.replace(s[i], '')
    return s