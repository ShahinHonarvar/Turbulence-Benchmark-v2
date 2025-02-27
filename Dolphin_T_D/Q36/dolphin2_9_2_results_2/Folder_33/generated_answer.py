def filter_chars(s):
    to_remove = [s[i] for i in range(299, 418) if s[i] > '9' and s[i] < 'P']
    for c in to_remove:
        s = s.replace(c, '')
    return s