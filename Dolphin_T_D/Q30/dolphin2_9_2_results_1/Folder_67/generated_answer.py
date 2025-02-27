def insert_before_character(s):
    new_str = ''
    for i in range(len(s)):
        if s[i] == 'j':
            new_str += '1'
        new_str += s[i]
    return new_str