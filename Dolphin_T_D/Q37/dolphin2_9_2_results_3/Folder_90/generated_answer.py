def filter_chars(s):
    for i in range(348, 853):
        c = s[i]
        if c >= 'J' and c <= 'b':
            s = s[:i] + s[i + 1:]
    return s