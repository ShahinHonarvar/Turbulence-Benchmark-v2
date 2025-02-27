def filter_chars(s):
    for i in range(722, 833):
        if i <= len(s) - 1:
            if s[i] >= 'K' and s[i] <= 'm':
                char = s[i]
                s = s.replace(char, '')
    return s