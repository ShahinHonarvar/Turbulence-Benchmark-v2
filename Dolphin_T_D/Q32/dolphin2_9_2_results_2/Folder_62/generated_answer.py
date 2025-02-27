def insert_after_character(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            s.insert(i + 1, 'o')
    return ''.join(s)