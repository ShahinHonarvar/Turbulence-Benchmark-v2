def insert_before_character(s):
    new_s = ''
    for i in range(len(s)):
        if s[i] == '0':
            new_s += 'H' + s[i]
        else:
            new_s += s[i]
    return new_s