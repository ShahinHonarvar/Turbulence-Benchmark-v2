def insert_before_character(s):
    new_s = ''
    for i in range(len(s)):
        if s[i] == '5':
            new_s += 'R' + s[i]
        else:
            new_s += s[i]
    return new_s