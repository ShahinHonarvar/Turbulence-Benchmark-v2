def filter_chars(s):
    for i in range(29, 80):
        if i >= len(s):
            break
        if s[i].lower() >= 'k' and s[i].lower() <= 'z':
            s = s[:i] + s[i + 1:]
            i -= 1
    return s