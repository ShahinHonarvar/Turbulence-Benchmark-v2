def insert_after_character(s):
    i = 0
    while i < len(s):
        if s[i] == ' ':
            s = s[:i + 1] + ' ' + s[i + 1:]
        i += 1
    return s