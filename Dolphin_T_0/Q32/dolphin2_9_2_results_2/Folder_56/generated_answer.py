def insert_after_character(s):
    out = ''
    for i, c in enumerate(s):
        if c == 'I':
            out = s[:i + 1] + 'i' + s[i + 1:]
    return out