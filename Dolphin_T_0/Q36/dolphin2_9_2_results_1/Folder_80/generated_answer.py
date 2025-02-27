def filter_chars(s):
    for i in range(54, 92):
        if s[i] > 'J' and s[i] < 'X':
            s = s[:i] + s[i + 1:]
    return s