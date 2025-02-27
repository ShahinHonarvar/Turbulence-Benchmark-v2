def insert_after_character(s):
    new_s = ''
    for i in range(len(s)):
        if s[i] == 'i':
            new_s += s[i]
            new_s += 'I'
        else:
            new_s += s[i]
    return new_s