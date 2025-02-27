def insert_after_character(s):
    new_string = ''
    for i in range(len(s)):
        new_string += s[i]
        if s[i] == 'A':
            new_string += 'H'
    return new_string