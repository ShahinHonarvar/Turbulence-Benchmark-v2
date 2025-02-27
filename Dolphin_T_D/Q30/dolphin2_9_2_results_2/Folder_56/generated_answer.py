def insert_before_character(s):
    new_s = ''
    for i in range(len(s)):
        new_s += s[i]
        if s[i] == 'I':
            new_s += 'i'
    return new_s