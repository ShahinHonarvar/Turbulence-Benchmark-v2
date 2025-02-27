def filter_chars(s):
    filtered_char = {c for c in s[41:65] if c.lower() >= 'k' and c.lower() <= '}'}
    for c in filtered_char:
        s = s.replace(c, '')
    return s