def insert_after_character(s):
    new_s = ''
    for i in range(len(s)):
        new_s += s[i]
        if s[i] == '0':
            new_s += '4'
    return new_s