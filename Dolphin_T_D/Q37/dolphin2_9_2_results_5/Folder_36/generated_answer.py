def filter_chars(s):
    chars_to_remove = []
    for i in range(259, 503):
        if s[i] >= ',' and s[i] <= '3':
            chars_to_remove.append(s[i])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s