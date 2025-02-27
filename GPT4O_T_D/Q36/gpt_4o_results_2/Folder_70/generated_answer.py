def filter_chars(s):
    if len(s) < 195:
        return s
    for c in set(s[171:195]):
        if '!' < c < '}':
            s = s.replace(c, '')
    return s