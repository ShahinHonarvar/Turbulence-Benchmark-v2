def insert_after_character(s):
    new_s = ''
    for i in range(len(s)):
        if s[i] == '9':
            new_s += s[i] + 'h'
        else:
            new_s += s[i]
    return new_s