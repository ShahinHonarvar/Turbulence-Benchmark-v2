def insert_before_character(s):
    new_string = ''
    for i in range(len(s)):
        if s[i] == 'U':
            new_string += 'a' + s[i]
        else:
            new_string += s[i]
    return new_string