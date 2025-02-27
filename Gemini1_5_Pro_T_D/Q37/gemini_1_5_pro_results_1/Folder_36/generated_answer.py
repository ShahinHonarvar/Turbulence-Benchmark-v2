def filter_chars(s):
    for i in range(259, 503):
        if i <= len(s) - 1:
            if s[i] >= ',' and s[i] <= '3':
                s = s.replace(s[i], '')
    return s