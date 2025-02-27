def filter_chars(s):
    for c in range(323, 526):
        if s[c] > ')' and s[c] < 'O':
            s = ''.join((ch for ch in s if ch != s[c]))
    return s