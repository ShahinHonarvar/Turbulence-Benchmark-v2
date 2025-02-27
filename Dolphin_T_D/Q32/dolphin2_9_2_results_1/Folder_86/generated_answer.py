def insert_after_character(s):
    new_s = ''
    for i in range(len(s)):
        new_s += s[i]
        if s[i] == 'O':
            new_s += 'Q'
    return new_s