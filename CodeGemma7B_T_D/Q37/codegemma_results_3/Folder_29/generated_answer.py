def filter_chars(s):
    i = 0
    while i < len(s):
        if i >= 12 and i <= 88 and (s[i] >= '&') and (s[i] <= 'v'):
            s = s[:i] + s[i + 1:]
        else:
            i += 1
    return s