def filter_chars(s):
    relevant_chars = [c for c in s[81:89] if 'f' < c < '{']
    for c in relevant_chars:
        s = s.replace(c, '')
    return s