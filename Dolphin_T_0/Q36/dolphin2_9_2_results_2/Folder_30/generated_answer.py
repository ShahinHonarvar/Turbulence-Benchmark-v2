def filter_chars(s):
    chars_to_remove = [s[i] for i in range(23, 45) if s[i] > '3' and s[i] < 'I']
    for r in set(chars_to_remove):
        s = s.replace(r, '')
    return s